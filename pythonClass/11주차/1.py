def read_file_to_list(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            # 파일의 모든 줄을 읽어서 리스트로 변환
            lines = file.readlines()
            # 각 줄의 끝에 있는 줄바꿈 문자를 제거
            lines = [line.strip() for line in lines]
        return lines
    except FileNotFoundError:
        print(f"파일을 찾을 수 없습니다: {file_path}")
        return []
    except IOError:
        print(f"파일을 읽는 도중 오류가 발생했습니다: {file_path}")
        return []

data = tuple(read_file_to_list('password.txt'))


while True:
    if data == '':
        print('관리자 정보를 조회할 수 없습니다.')
        break
    print('관리자 정보를 성공적으로 조회하였습니다.')

    user_input_ID = input("아이디 입력:")
    user_input_PW = input("비밀번호 입력:")

    if user_input_ID == data[0] and user_input_PW == data[2]:
        print("로그인에 성공했습니다.")
        break
    print("아이디 또는 비밀번호가 잘못 입력되었습니다.")