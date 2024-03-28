-- 코드를 입력하세요
SELECT MEMBER_ID
    , MEMBER_NAME
    , GENDER                
    , DATE_FORMAT(DATE_OF_BIRTH, '%Y-%m-%d') AS DATE_OF_BIRTH   # # 3. ID, 이름, 성별, 생년월일을
    FROM MEMBER_PROFILE                                         # 0. member_profile 테이블에서
    WHERE MONTH(DATE_OF_BIRTH) = 3                              # 1. 생일이 3월인
        AND GENDER = 'W'                                        # 2. 여성 회원의
        AND TLNO IS NOT NULL                                    # 4. 근데 이제 전번 없으면 제외하고
        ORDER BY MEMBER_ID ASC;                                 # 5. 아이디 오름차순으로 조회