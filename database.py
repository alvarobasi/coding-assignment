from DirGraph import TreeNode


class Database(object):
    """
    docstring
    """

    def __init__(self, root):
        """
        docstring
        """
        self.__root_node = TreeNode(root)
        self.__extract_dict = dict()
        self.__status_dict = dict()

    def add_nodes(self, new_nodes):
        """
        docstring
        """
        for ID, parent in new_nodes:
            self.__add_single_node(ID, parent, self.__root_node)

            for image, labels in self.__extract_dict.items():
                prev_status = self.__status_dict[image]
                if len(labels) > 0:
                    for label in labels:
                        current_status = "invalid"
                        match_node = self.__get_node(label)
                        if match_node:
                            if match_node.is_root():
                                if match_node.get_name() == parent and prev_status != "coverage_staged":
                                    current_status = "granularity_staged"
                                    prev_status = current_status
                                elif prev_status != "granularity_staged" and prev_status != "coverage_staged":
                                    current_status = "valid"
                                    prev_status = current_status
                                else:
                                    current_status = prev_status
                            elif match_node.get_parent().get_name() == parent:
                                current_status = "coverage_staged"
                                break
                            elif match_node.get_name() == parent and prev_status != "coverage_staged":
                                current_status = "granularity_staged"
                                prev_status = current_status
                            elif prev_status != "granularity_staged" and prev_status != "coverage_staged":
                                current_status = "valid"
                                prev_status = current_status
                            else:
                                current_status = prev_status
                        else:
                            break
                else:
                    current_status = "valid"
                self.__status_dict[image] = current_status

    def add_extract(self, new_extracts):
        """
        docstring
        """
        self.__extract_dict.update(new_extracts)

        # Checking whether the status of each extract has changed after the dictionary update.
        for image, labels in self.__extract_dict.items():
            if len(labels) > 0:
                prev_status = "invalid"
                for label in labels:
                    current_status = "invalid"
                    match_node = self.__get_node(label)
                    if match_node:
                        if match_node.has_children():
                            current_status = "granularity_staged"
                            prev_status = current_status
                        elif prev_status != "granularity_staged":
                            current_status = "valid"
                            prev_status = current_status
                        else:
                            break
            else:
                current_status = "valid"
            self.__status_dict[image] = current_status

    def print(self):
        """
        docstring
        """
        self.__root_node.print()

    def get_graph(self):
        """
        docstring
        """
        return self.__root_node

    def __get_node(self, name, root=None):
        """
        docstring
        """
        if not root:
            root = self.__root_node

        found_node = None
        if root.get_name() == name:
            found_node = root
        else:
            if root.has_children():
                node = root.left_most_child()
                while not found_node and node is not None:
                    found_node = self.__get_node(name, node)
                    node = node.get_right_sibling()

        return found_node

    def __add_single_node(self, ID, parent, root):
        """
        docstring
        """
        added = False
        if root.get_name() == parent:
            if ID not in root.get_children_list():
                root.add_child(TreeNode(ID))
                added = True
        else:
            if root.has_children():
                node = root.left_most_child()
                while not added and node is not None:
                    self.__add_single_node(ID, parent, node)
                    node = node.get_right_sibling()

    def get_extract_status(self):
        """
        docstring
        """
        return self.__status_dict

    def get_extract_list(self):
        """
        docstring
        """
        return self.__extract_dict
