from datetime import datetime

if __name__ == '__main__':
    now = datetime.now()
    print(
        format(now, '%H:%M:%S')
    )
    print(
        'It is now {:%I:%M %p}'.format(now)
    )

