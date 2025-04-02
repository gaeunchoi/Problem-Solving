from collections import Counter
def solution(points, routes):
    conflict = 0
    robot_cnt = len(routes)
    max_robot_move_routes = 0

    robot_move_routes = [[] for _ in range(robot_cnt)]

    for i in range(len(routes)):
        # [[2, 2], [2, 3], [2, 7], [6, 6], [5, 2]]
        # [[2, 3, 4, 5], [1, 3, 4, 5]]
        for j in range(len(routes[i])-1):
            start_x, start_y = points[routes[i][j]-1]
            end_x, end_y = points[routes[i][j+1]-1]

            robot_move_x, robot_move_y = end_x - start_x, end_y - start_y

            if j == 0:
                robot_move_routes[i].append([start_x, start_y])

            for k in range(abs(robot_move_x) + abs(robot_move_y)):
                if robot_move_x > 0:
                    robot_move_routes[i].append([start_x+1, start_y])
                    start_x += 1
                    robot_move_x -= 1
                elif robot_move_x < 0:
                    robot_move_routes[i].append([start_x-1, start_y])
                    start_x -= 1
                    robot_move_x += 1
                else:
                    if robot_move_y > 0:
                        robot_move_routes[i].append([start_x, start_y+1])
                        start_y += 1
                        robot_move_y -= 1
                    elif robot_move_y < 0:
                        robot_move_routes[i].append([start_x, start_y-1])
                        start_y -= 1
                        robot_move_y += 1

            max_robot_move_routes = max(max_robot_move_routes, len(robot_move_routes[i]))

    for i in range(max_robot_move_routes):
        current_time_robot_pos = []

        for j in range(robot_cnt):
            if i <= len(robot_move_routes[j])-1:
                current_time_robot_pos.append(tuple(robot_move_routes[j][i]))

        validate_current_pos = Counter(current_time_robot_pos)
        for pos in validate_current_pos.values():
            if pos >= 2:
                conflict += 1

    return conflict
