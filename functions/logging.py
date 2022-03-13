def record_nodes(node_set:set, file_path:str) -> None:
    """
        Description:
            Records the node locations for further use

        Arguments:
            - node_type : `str` type of the node
            - node_set : `set` set storing the nodes
            - file_path : `str` file to write into 
    """
    with open(file_path, 'w') as file:
        for node in node_set:
            file.write('{}\n'.format(node))