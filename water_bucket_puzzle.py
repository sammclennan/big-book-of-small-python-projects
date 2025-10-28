# Water bucket puzzle

import sys


def get_player_action():
    print("""You can:
  (F)ill the bucket
  (E)mpty the bucket
  (P)our one bucket into another
  (Q)uit
    """)
    while True:
        response = input('> ').strip().upper()
        if response == 'Q':
            print('Thanks for playing!')
            sys.exit()
        elif response in ('F', 'E', 'P'):
            return response
        else:
            print('Choose from F, E, P, or Q to quit.')
        

def get_bucket(second_bucket=False):
    while True:
        print(f'Select a bucket{' to pour into' if second_bucket else ''}: 8, 5, 3')
        response = input('> ').strip().upper()
        if response == 'Q':
            print('Thanks for playing!')
            sys.exit()
        elif response in ('8', '5', '3'):
            return int(response)
        

def change_levels(bucket, action, bucket_data):
    bucket_data = bucket_data
    # Fill bucket
    if action == 'F':
        bucket_data[bucket] = bucket
    # Empty bucket
    elif action == 'E':
        bucket_data[bucket] = 0
    # Pour water between buckets
    else:
        bucket_2 = get_bucket(second_bucket=True)
        free_space = bucket_2 - bucket_data[bucket_2]
        if free_space:
            bucket_data[bucket], bucket_data[bucket_2] = bucket_data[bucket] - min(bucket_data[bucket], free_space), bucket_data[bucket_2] + min(bucket_data[bucket], free_space)
    
    return bucket_data


def draw_buckets(bucket_data):
    for i in range(max(bucket_data), 0, -1):
        for number, level in bucket_data.items():
            if i <= number:
                print(f'{i:>2}|{' ' * 6 if i > level else 'W' * 6}|', end=' ')
            else:
                print(' ' * 10, end=' ')
        print()
    print('  +------+ ' * 3)
    for number in bucket_data.keys():
        print(f'{number}L'.center(11), end='')
    print()


def main():
    buckets = {
            8: 0,
            5: 0,
            3: 0,
        }
    
    steps = 0

    while True:
        print('Try to get 4L of water into one of these buckets:')

        draw_buckets(buckets)

        # Check for winning condition
        for bucket_number in buckets:
            if buckets[bucket_number] == 4:
                print(f'Good job! You solved it in {steps} steps!')
                sys.exit()

        # Get playing input
        action = get_player_action()
        bucket_number = get_bucket()

        # Update bucket levels
        buckets = change_levels(bucket_number, action, buckets)

        steps += 1


if __name__ == '__main__':
    main()