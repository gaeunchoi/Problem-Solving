def solution(numbers, hand):
    answer = []
    left = [1, 4, 7]
    right = [3, 6, 9]
    left_pos = [3, 0]
    right_pos = [3, 2]
    
    def add_left(row, col):
        answer.append('L')
        left_pos[0], left_pos[1] = row, col
        
    def add_right(row, col):
        answer.append('R')
        right_pos[0], right_pos[1] = row, col
        
    for number in numbers:
        if number == 0:
            row, col = 3, 1
        else:
            row, col = (number - 1) // 3, (number - 1) % 3
        
        if number in left:
            add_left(row, col)
        elif number in right:
            add_right(row, col)
        else:
            left_dis = abs(left_pos[0] - row) + abs(left_pos[1] - col)
            right_dis = abs(right_pos[0] - row) + abs(right_pos[1] - col)
            
            if left_dis < right_dis:
                add_left(row, col)
            elif right_dis < left_dis:
                add_right(row, col)
            else:
                if hand == 'left':
                    add_left(row, col)
                else:
                    add_right(row, col)
                
    return "".join(answer)
            