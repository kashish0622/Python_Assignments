if __name__ == '__main__':
    from util import is_valid
    n = int(input("Enter number of emails: "))
    emails = [input().strip() for _ in range(n)]
    valid_emails = sorted(filter(is_valid, emails))
    print(valid_emails)
