
def validate_email(email):
    if email:
        if email.count('@') == 0 or email.count('.') == 0:
            return False
        if email.count('@') == 1 and email.count('.') == 1:
            username,url=email.split('@')
            website,extension=url.split('.')
            if username == '' or website == '' or extension == '':
                return False
            if len(extension) > 3:
                return False
            return True
        else:
            return False

def filter_validate_email(email):
    return list(filter(validate_email,email))


def main():
    n=int(input("Enter how many emails: "))
    emails=[]
    print("Enter ",n, " emails:")
    for _ in range(n):
        emails.append(input())
    valid_emails=filter_validate_email(emails)
    print(valid_emails)

if __name__=='__main__':
    main()