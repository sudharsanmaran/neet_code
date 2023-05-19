from typing import List


def carFleet(target: int, position: List[int], speed: List[int]) -> int:
    """
    t O(n * (target - n'th_pos / speed(n)) * prev_cars)  / s O(target - pos / speed)
    """
    subsequent_pos, possible_fleet, _break = {}, len(position), False
    for i, val in enumerate(zip(position, speed)):
        pos, speed = val
        step = 0
        # all possible position for current car
        while pos <= target:
            # ignore initial position for collision
            if step and step in subsequent_pos:
                # check other cars at the same position
                for num in subsequent_pos[step]:
                    if pos >= num:
                        if pos - speed <= num:
                            possible_fleet -= 1
                            _break = True
                            break

                if _break:
                    break
            else:
                subsequent_pos[step] = [*subsequent_pos.get(step, []), pos]
            step += 1
            pos += speed

    return possible_fleet


def car_fleet(target: int, position: List[int], speed: List[int]) -> int:
    """avoid checking all possible positions by sorting the cars based on their position,
    and we can use speed time eqn to get time of the car at O(1),
    so just need to find if the cars get collide or not, not the exact position of collision

    n = position + speed
    t O(n * log(n) / s O(n)
    """

    allowed_time, possible_fleet = 0, len(position)
    for cur_pos, speed in sorted((pos, speed) for pos, speed in zip(position, speed))[::-1]:
        time = (target - cur_pos) / speed
        if allowed_time and time <= allowed_time:
            possible_fleet -= 1
        else:
            allowed_time = time
    return possible_fleet


if __name__ == '__main__':
    print(car_fleet(target=12, position=[10, 8, 0, 5, 3], speed=[2, 4, 1, 1, 3]))
    print(car_fleet(target=10, position=[3], speed=[3]))
    print(car_fleet(target=100, position=[0, 2, 4], speed=[4, 2, 1]))
    print(car_fleet(target=20, position=[6, 2, 17], speed=[3, 9, 2]))
