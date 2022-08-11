from structs.node import Gateway

def add_manually(gateway_set:set, distance_threshold:float) -> set:
    """
        Description:
            Adds gateways to the grid manually, according to the
            coverage distance

        Arguments:
            - gateway_set : `set` stores `Gateway` objects
            - distance_threshold : `float` upper limit of distance
            between nodes so that can communicate

        Returns:
            `set` : stores `Gateway` objects
    """

    if distance_threshold == 1:
        gateway_set.add(Gateway(len(gateway_set), 0, 14, 0))
        gateway_set.add(Gateway(len(gateway_set), 8, 24, 0))
        gateway_set.add(Gateway(len(gateway_set), 12, 19, 0))
        gateway_set.add(Gateway(len(gateway_set), 16, 33, 0))
        gateway_set.add(Gateway(len(gateway_set), 18, 38, 0))
        gateway_set.add(Gateway(len(gateway_set), 21, 41, 0))
        gateway_set.add(Gateway(len(gateway_set), 27, 44, 0))
        gateway_set.add(Gateway(len(gateway_set), 30, 46, 0))
        gateway_set.add(Gateway(len(gateway_set), 33, 49, 0))
        gateway_set.add(Gateway(len(gateway_set), 35, 47, 0))
        gateway_set.add(Gateway(len(gateway_set), 35, 53, 0))
        gateway_set.add(Gateway(len(gateway_set), 36, 56, 0))
        gateway_set.add(Gateway(len(gateway_set), 36, 0, 0))
        gateway_set.add(Gateway(len(gateway_set), 36, 3, 0))
        gateway_set.add(Gateway(len(gateway_set), 42, 41, 0))
        gateway_set.add(Gateway(len(gateway_set), 43, 61, 0))
        gateway_set.add(Gateway(len(gateway_set), 45, 19, 0))
        gateway_set.add(Gateway(len(gateway_set), 47, 38, 0))
        gateway_set.add(Gateway(len(gateway_set), 45, 49, 0))
        gateway_set.add(Gateway(len(gateway_set), 47, 49, 0))
        gateway_set.add(Gateway(len(gateway_set), 50, 50, 0))
        gateway_set.add(Gateway(len(gateway_set), 54, 51, 0))
        gateway_set.add(Gateway(len(gateway_set), 58, 100, 0))
        gateway_set.add(Gateway(len(gateway_set), 58, 49, 0))
        gateway_set.add(Gateway(len(gateway_set), 60, 50, 0))
        gateway_set.add(Gateway(len(gateway_set), 62, 49, 0))
        gateway_set.add(Gateway(len(gateway_set), 63, 58, 0))
        gateway_set.add(Gateway(len(gateway_set), 64, 49, 0))
        gateway_set.add(Gateway(len(gateway_set), 68, 44, 0))
        gateway_set.add(Gateway(len(gateway_set), 69, 43, 0))
        gateway_set.add(Gateway(len(gateway_set), 69, 19, 0))
        gateway_set.add(Gateway(len(gateway_set), 70, 32, 0))
        gateway_set.add(Gateway(len(gateway_set), 71, 28, 0))
        gateway_set.add(Gateway(len(gateway_set), 72, 44, 0))
        gateway_set.add(Gateway(len(gateway_set), 77, 25, 0))
        gateway_set.add(Gateway(len(gateway_set), 83, 49, 0))
        gateway_set.add(Gateway(len(gateway_set), 87, 29, 0))
        gateway_set.add(Gateway(len(gateway_set), 91, 32, 0))
        gateway_set.add(Gateway(len(gateway_set), 92, 49, 0))
        gateway_set.add(Gateway(len(gateway_set), 95, 33, 0))

    elif distance_threshold == 3 or distance_threshold == 2:
        gateway_set.add(Gateway(len(gateway_set), 0, 14, 0))
        gateway_set.add(Gateway(len(gateway_set), 8, 24, 0))
        gateway_set.add(Gateway(len(gateway_set), 12, 19, 0))
        gateway_set.add(Gateway(len(gateway_set), 16, 33, 0))
        gateway_set.add(Gateway(len(gateway_set), 20, 41, 0))
        gateway_set.add(Gateway(len(gateway_set), 27, 44, 0))
        gateway_set.add(Gateway(len(gateway_set), 30, 46, 0))
        gateway_set.add(Gateway(len(gateway_set), 35, 1.5, 0))
        gateway_set.add(Gateway(len(gateway_set), 34.5, 49, 0))
        gateway_set.add(Gateway(len(gateway_set), 35, 54.5, 0))
        gateway_set.add(Gateway(len(gateway_set), 42, 41, 0))
        gateway_set.add(Gateway(len(gateway_set), 43, 60, 0))
        gateway_set.add(Gateway(len(gateway_set), 45, 19, 0))
        gateway_set.add(Gateway(len(gateway_set), 47, 38, 0))
        gateway_set.add(Gateway(len(gateway_set), 46, 48, 0))
        gateway_set.add(Gateway(len(gateway_set), 50, 50, 0))
        gateway_set.add(Gateway(len(gateway_set), 55, 50, 0))
        gateway_set.add(Gateway(len(gateway_set), 58, 100, 0))
        gateway_set.add(Gateway(len(gateway_set), 60, 50, 0))
        gateway_set.add(Gateway(len(gateway_set), 62, 58, 0))
        gateway_set.add(Gateway(len(gateway_set), 68, 43, 0))
        gateway_set.add(Gateway(len(gateway_set), 70, 20, 0))
        gateway_set.add(Gateway(len(gateway_set), 71, 28, 0))
        gateway_set.add(Gateway(len(gateway_set), 72, 44, 0))
        gateway_set.add(Gateway(len(gateway_set), 77, 25, 0))
        gateway_set.add(Gateway(len(gateway_set), 83, 49, 0))
        gateway_set.add(Gateway(len(gateway_set), 87, 30, 0))
        gateway_set.add(Gateway(len(gateway_set), 90, 32, 0))
        gateway_set.add(Gateway(len(gateway_set), 92, 50, 0))
        
        if distance_threshold == 2:
            gateway_set.add(Gateway(len(gateway_set), 50, 50, 0))
            gateway_set.add(Gateway(len(gateway_set), 72, 44, 0))
            gateway_set.add(Gateway(len(gateway_set), 87, 30, 0))
            gateway_set.add(Gateway(len(gateway_set), 90, 32, 0))

    elif distance_threshold == 5 or distance_threshold == 4:
        gateway_set.add(Gateway(len(gateway_set), 0, 14, 0))
        gateway_set.add(Gateway(len(gateway_set), 8, 23, 0))
        gateway_set.add(Gateway(len(gateway_set), 12, 19, 0))
        gateway_set.add(Gateway(len(gateway_set), 18, 32, 0))
        gateway_set.add(Gateway(len(gateway_set), 21, 42, 0))
        gateway_set.add(Gateway(len(gateway_set), 30, 45, 0))
        gateway_set.add(Gateway(len(gateway_set), 35, 1, 0))
        gateway_set.add(Gateway(len(gateway_set), 35, 48, 0))
        gateway_set.add(Gateway(len(gateway_set), 37, 55, 0))
        gateway_set.add(Gateway(len(gateway_set), 44, 60, 0))
        gateway_set.add(Gateway(len(gateway_set), 44.5, 40, 0))
        gateway_set.add(Gateway(len(gateway_set), 47, 20, 0))
        gateway_set.add(Gateway(len(gateway_set), 58, 98, 0))
        gateway_set.add(Gateway(len(gateway_set), 65, 60, 0))
        gateway_set.add(Gateway(len(gateway_set), 70, 20, 0))
        gateway_set.add(Gateway(len(gateway_set), 72, 27, 0))
        gateway_set.add(Gateway(len(gateway_set), 80, 24, 0))
        gateway_set.add(Gateway(len(gateway_set), 83, 49, 0))
        gateway_set.add(Gateway(len(gateway_set), 93, 49, 0))

        if distance_threshold == 4:
            gateway_set.add(Gateway(len(gateway_set), 61, 50, 0))

    elif distance_threshold == 7 or distance_threshold == 6:
        gateway_set.add(Gateway(len(gateway_set), 0, 14, 0))
        gateway_set.add(Gateway(len(gateway_set), 10, 20, 0))
        gateway_set.add(Gateway(len(gateway_set), 23, 43, 0))
        gateway_set.add(Gateway(len(gateway_set), 34, 48, 0))
        gateway_set.add(Gateway(len(gateway_set), 37, 3, 0))
        gateway_set.add(Gateway(len(gateway_set), 37, 55, 0))
        gateway_set.add(Gateway(len(gateway_set), 44, 40, 0))
        gateway_set.add(Gateway(len(gateway_set), 46, 20, 0))
        gateway_set.add(Gateway(len(gateway_set), 46, 60, 0))
        gateway_set.add(Gateway(len(gateway_set), 58, 98, 0))
        gateway_set.add(Gateway(len(gateway_set), 65, 60, 0))
        gateway_set.add(Gateway(len(gateway_set), 70, 20, 0))
        gateway_set.add(Gateway(len(gateway_set), 80, 22, 0))
        gateway_set.add(Gateway(len(gateway_set), 83, 49, 0))
        gateway_set.add(Gateway(len(gateway_set), 93, 49, 0))

        if distance_threshold == 6:
            gateway_set.add(Gateway(len(gateway_set), 18, 30, 0))

    elif distance_threshold == 8:
        gateway_set.add(Gateway(len(gateway_set), 0, 14, 0))
        gateway_set.add(Gateway(len(gateway_set), 10, 20, 0))
        gateway_set.add(Gateway(len(gateway_set), 26, 44, 0))
        gateway_set.add(Gateway(len(gateway_set), 37, 3, 0))
        gateway_set.add(Gateway(len(gateway_set), 38, 50, 0))
        gateway_set.add(Gateway(len(gateway_set), 44, 40, 0))
        gateway_set.add(Gateway(len(gateway_set), 46, 20, 0))
        gateway_set.add(Gateway(len(gateway_set), 46, 60, 0))
        gateway_set.add(Gateway(len(gateway_set), 58, 98, 0))
        gateway_set.add(Gateway(len(gateway_set), 65, 60, 0))
        gateway_set.add(Gateway(len(gateway_set), 75, 21, 0))
        gateway_set.add(Gateway(len(gateway_set), 90, 50, 0))

    elif distance_threshold == 9 or distance_threshold == 10:
        gateway_set.add(Gateway(len(gateway_set), 6, 18, 0))
        gateway_set.add(Gateway(len(gateway_set), 37, 50, 0))
        gateway_set.add(Gateway(len(gateway_set), 37, 3, 0))
        gateway_set.add(Gateway(len(gateway_set), 44, 20, 0))
        gateway_set.add(Gateway(len(gateway_set), 44, 63, 0))
        gateway_set.add(Gateway(len(gateway_set), 45, 39, 0))
        gateway_set.add(Gateway(len(gateway_set), 62, 98, 0))
        gateway_set.add(Gateway(len(gateway_set), 65, 62, 0))
        gateway_set.add(Gateway(len(gateway_set), 75, 21, 0))
        gateway_set.add(Gateway(len(gateway_set), 90, 50, 0))
    
    return gateway_set