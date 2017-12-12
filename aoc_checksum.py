import io


def aoc_checksum(input):
    checksum = 0
    for _l in io.StringIO(input):
        _l = _l.strip()
        if(_l):
            nums = list(map(int, _l.split()))
            checksum += max(nums) - min(nums)
    return checksum

def get_checksum2(nums):
    ''' Looks through a list of ints and finds the first set that are evenly divisible'''
    if len(nums) >= 2:
        nums = sorted(nums)
        print('Looking at {}'.format(nums))
        this_num = nums[0]
        for x in nums[1:]:
            if x % this_num == 0:
                print('Found {} / {} is {}'.format(x, this_num, x / this_num))
                return x / this_num
        return get_checksum2(nums[1:])
    else:
        return 0
   
def aoc_checksum_2(input):
    checksum = 0
    for _l in io.StringIO(input):
        _l = _l.strip()
        if(_l):
            nums = list(map(int, _l.split()))
            checksum += get_checksum2(nums)
    return checksum


if __name__ == '__main__':
    print('hello world')
    with open('./test_input', 'r') as f:
        test_input = f.read()
    print('Input is\n{}\n'.format(''.join('{}'.format(l) for l in test_input)))
    print('Checksum of input is {}'.format(aoc_checksum(test_input)))
    print('Checksum2 of input is {}'.format(aoc_checksum_2(test_input)))
