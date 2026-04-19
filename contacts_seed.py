import json
from collections import Counter

contacts = []

emergency = [
    {"id": "e001", "name": "경찰청 신고", "category": "긴급", "subcategory": "신고", "tel": "112", "ars": "", "hours": "24시간", "official": True},
    {"id": "e002", "name": "소방서/구급", "category": "긴급", "subcategory": "신고", "tel": "119", "ars": "", "hours": "24시간", "official": True},
    {"id": "e003", "name": "범죄신고/여성안전", "category": "긴급", "subcategory": "신고", "tel": "117", "ars": "", "hours": "24시간", "official": True},
    {"id": "e004", "name": "자살예방상담전화", "category": "긴급", "subcategory": "상담", "tel": "1393", "ars": "", "hours": "24시간", "official": True},
    {"id": "e005", "name": "정부민원안내", "category": "긴급", "subcategory": "민원", "tel": "110", "ars": "", "hours": "24시간", "official": True},
]

government = [
    {"id": "g001", "name": "국세청 세금신고", "category": "관공서", "subcategory": "세금", "tel": "126", "ars": "1→세금신고/2→세무조사", "hours": "평일 09:00~18:00", "official": True},
    {"id": "g002", "name": "관세청", "category": "관공서", "subcategory": "관세", "tel": "125", "ars": "", "hours": "평일 09:00~18:00", "official": True},
    {"id": "g003", "name": "출입국외국인정책본부", "category": "관공서", "subcategory": "출입국", "tel": "1345", "ars": "", "hours": "평일 09:00~18:00", "official": True},
    {"id": "g004", "name": "고용노동부", "category": "관공서", "subcategory": "노동", "tel": "1350", "ars": "1→임금체불/2→실업급여", "hours": "평일 09:00~18:00", "official": True},
    {"id": "g005", "name": "국민권익위원회", "category": "관공서", "subcategory": "민원", "tel": "1398", "ars": "", "hours": "평일 09:00~18:00", "official": True},
    {"id": "g006", "name": "환경부 환경민원", "category": "관공서", "subcategory": "환경", "tel": "128", "ars": "", "hours": "24시간", "official": True},
    {"id": "g007", "name": "식품의약품안전처", "category": "관공서", "subcategory": "식약", "tel": "1577-1255", "ars": "", "hours": "평일 09:00~18:00", "official": True},
    {"id": "g008", "name": "국토교통부 콜센터", "category": "관공서", "subcategory": "건설/교통", "tel": "1599-0001", "ars": "", "hours": "평일 09:00~18:00", "official": True},
    {"id": "g009", "name": "보건복지부 콜센터", "category": "관공서", "subcategory": "복지", "tel": "129", "ars": "", "hours": "24시간", "official": True},
    {"id": "g010", "name": "교육부 교육민원", "category": "관공서", "subcategory": "교육", "tel": "02-6222-6060", "ars": "", "hours": "평일 09:00~18:00", "official": True},
]

public_org = [
    {"id": "p001", "name": "국민건강보험공단", "category": "공공기관", "subcategory": "건강보험", "tel": "1577-1000", "ars": "1→보험료/2→급여/3→자격", "hours": "평일 09:00~18:00", "official": True},
    {"id": "p002", "name": "국민연금공단", "category": "공공기관", "subcategory": "연금", "tel": "1355", "ars": "1→연금/2→보험료", "hours": "평일 09:00~18:00", "official": True},
    {"id": "p003", "name": "근로복지공단", "category": "공공기관", "subcategory": "산재/고용", "tel": "1588-0075", "ars": "", "hours": "평일 09:00~18:00", "official": True},
    {"id": "p004", "name": "건강보험심사평가원", "category": "공공기관", "subcategory": "의료비", "tel": "1644-2000", "ars": "", "hours": "평일 09:00~18:00", "official": True},
    {"id": "p005", "name": "한국전력공사", "category": "공공기관", "subcategory": "전기", "tel": "123", "ars": "1→고장신고/2→요금문의", "hours": "24시간(고장)", "official": True},
    {"id": "p006", "name": "한국가스공사", "category": "공공기관", "subcategory": "가스", "tel": "1544-4500", "ars": "", "hours": "24시간(긴급)", "official": True},
    {"id": "p007", "name": "한국도로공사", "category": "공공기관", "subcategory": "고속도로", "tel": "1588-2504", "ars": "", "hours": "24시간", "official": True},
    {"id": "p008", "name": "한국철도공사(코레일)", "category": "공공기관", "subcategory": "철도", "tel": "1544-7788", "ars": "1→예매/2→운행정보", "hours": "24시간", "official": True},
    {"id": "p009", "name": "서울교통공사", "category": "공공기관", "subcategory": "지하철", "tel": "1577-1234", "ars": "", "hours": "24시간", "official": True},
    {"id": "p010", "name": "LH한국토지주택공사", "category": "공공기관", "subcategory": "주택", "tel": "1600-1004", "ars": "", "hours": "평일 09:00~18:00", "official": True},
    {"id": "p011", "name": "한국소비자원", "category": "공공기관", "subcategory": "소비자보호", "tel": "1372", "ars": "", "hours": "평일 09:00~18:00", "official": True},
    {"id": "p012", "name": "금융감독원", "category": "공공기관", "subcategory": "금융민원", "tel": "1332", "ars": "1→은행/2→보험/3→증권", "hours": "평일 09:00~18:00", "official": True},
    {"id": "p013", "name": "한국장학재단", "category": "공공기관", "subcategory": "장학", "tel": "1599-2000", "ars": "", "hours": "평일 09:00~18:00", "official": True},
    {"id": "p014", "name": "고용보험 상담센터", "category": "공공기관", "subcategory": "실업급여", "tel": "1350", "ars": "2→실업급여", "hours": "평일 09:00~18:00", "official": True},
    {"id": "p015", "name": "도로교통공단", "category": "공공기관", "subcategory": "운전면허", "tel": "1577-1120", "ars": "", "hours": "평일 09:00~18:00", "official": True},
]

telecom = [
    {"id": "t001", "name": "SKT 고객센터", "category": "통신", "subcategory": "이동통신", "tel": "1599-0011", "ars": "0→상담원", "hours": "24시간", "official": True},
    {"id": "t002", "name": "KT 고객센터", "category": "통신", "subcategory": "이동통신", "tel": "100", "ars": "0→상담원", "hours": "24시간", "official": True},
    {"id": "t003", "name": "LG유플러스", "category": "통신", "subcategory": "이동통신", "tel": "101", "ars": "0→상담원", "hours": "24시간", "official": True},
    {"id": "t004", "name": "SK브로드밴드", "category": "통신", "subcategory": "인터넷", "tel": "106", "ars": "1→인터넷/2→IPTV", "hours": "24시간", "official": True},
    {"id": "t005", "name": "알뜰폰(MVNO) 공통", "category": "통신", "subcategory": "알뜰폰", "tel": "114", "ars": "", "hours": "24시간", "official": True},
]

finance = [
    {"id": "f001", "name": "KB국민은행", "category": "금융", "subcategory": "은행", "tel": "1588-9999", "ars": "0→상담원", "hours": "24시간", "official": True},
    {"id": "f002", "name": "신한은행", "category": "금융", "subcategory": "은행", "tel": "1599-8000", "ars": "0→상담원", "hours": "24시간", "official": True},
    {"id": "f003", "name": "우리은행", "category": "금융", "subcategory": "은행", "tel": "1588-5000", "ars": "0→상담원", "hours": "24시간", "official": True},
    {"id": "f004", "name": "하나은행", "category": "금융", "subcategory": "은행", "tel": "1599-1111", "ars": "0→상담원", "hours": "24시간", "official": True},
    {"id": "f005", "name": "NH농협은행", "category": "금융", "subcategory": "은행", "tel": "1588-2100", "ars": "0→상담원", "hours": "24시간", "official": True},
    {"id": "f006", "name": "IBK기업은행", "category": "금융", "subcategory": "은행", "tel": "1566-2566", "ars": "", "hours": "평일 09:00~18:00", "official": True},
    {"id": "f007", "name": "카카오뱅크", "category": "금융", "subcategory": "인터넷은행", "tel": "1599-3333", "ars": "", "hours": "24시간", "official": True},
    {"id": "f008", "name": "토스뱅크", "category": "금융", "subcategory": "인터넷은행", "tel": "1899-4905", "ars": "", "hours": "24시간", "official": True},
    {"id": "f009", "name": "케이뱅크", "category": "금융", "subcategory": "인터넷은행", "tel": "1522-1000", "ars": "", "hours": "24시간", "official": True},
    {"id": "f010", "name": "삼성카드", "category": "금융", "subcategory": "카드", "tel": "1588-8900", "ars": "분실→1번", "hours": "24시간(분실)", "official": True},
    {"id": "f011", "name": "현대카드", "category": "금융", "subcategory": "카드", "tel": "1577-6000", "ars": "분실→1번", "hours": "24시간(분실)", "official": True},
    {"id": "f012", "name": "KB국민카드", "category": "금융", "subcategory": "카드", "tel": "1588-1688", "ars": "분실→1번", "hours": "24시간(분실)", "official": True},
    {"id": "f013", "name": "신한카드", "category": "금융", "subcategory": "카드", "tel": "1544-7000", "ars": "분실→1번", "hours": "24시간(분실)", "official": True},
    {"id": "f014", "name": "롯데카드", "category": "금융", "subcategory": "카드", "tel": "1588-8100", "ars": "", "hours": "24시간(분실)", "official": True},
    {"id": "f015", "name": "NH농협카드", "category": "금융", "subcategory": "카드", "tel": "1644-4000", "ars": "", "hours": "24시간(분실)", "official": True},
    {"id": "f016", "name": "삼성생명", "category": "금융", "subcategory": "생명보험", "tel": "1588-3114", "ars": "1→보험금/2→계약", "hours": "평일 09:00~18:00", "official": True},
    {"id": "f017", "name": "한화생명", "category": "금융", "subcategory": "생명보험", "tel": "1588-6363", "ars": "", "hours": "평일 09:00~18:00", "official": True},
    {"id": "f018", "name": "교보생명", "category": "금융", "subcategory": "생명보험", "tel": "1588-1001", "ars": "", "hours": "평일 09:00~18:00", "official": True},
    {"id": "f019", "name": "삼성화재", "category": "금융", "subcategory": "손해보험", "tel": "1588-5114", "ars": "1→사고접수", "hours": "24시간(사고)", "official": True},
    {"id": "f020", "name": "현대해상", "category": "금융", "subcategory": "손해보험", "tel": "1588-5656", "ars": "", "hours": "24시간(사고)", "official": True},
    {"id": "f021", "name": "DB손해보험", "category": "금융", "subcategory": "손해보험", "tel": "1588-0100", "ars": "", "hours": "24시간(사고)", "official": True},
    {"id": "f022", "name": "KB손해보험", "category": "금융", "subcategory": "손해보험", "tel": "1544-0114", "ars": "", "hours": "24시간(사고)", "official": True},
    {"id": "f023", "name": "미래에셋증권", "category": "금융", "subcategory": "증권", "tel": "1588-6800", "ars": "", "hours": "평일 09:00~18:00", "official": True},
    {"id": "f024", "name": "삼성증권", "category": "금융", "subcategory": "증권", "tel": "1588-2323", "ars": "", "hours": "평일 09:00~18:00", "official": True},
    {"id": "f025", "name": "키움증권", "category": "금융", "subcategory": "증권", "tel": "1544-9000", "ars": "", "hours": "평일 09:00~18:00", "official": True},
]

it_electronics = [
    {"id": "i001", "name": "삼성전자 서비스", "category": "IT/전자", "subcategory": "전자제품", "tel": "1588-3366", "ars": "1→모바일/2→TV/3→가전", "hours": "평일 09:00~18:00", "official": True},
    {"id": "i002", "name": "LG전자 서비스", "category": "IT/전자", "subcategory": "전자제품", "tel": "1544-7777", "ars": "1→모바일/2→TV/3→가전", "hours": "평일 09:00~18:00", "official": True},
    {"id": "i003", "name": "Apple 고객지원", "category": "IT/전자", "subcategory": "전자제품", "tel": "0800-040-1548", "ars": "", "hours": "평일 09:00~18:00", "official": True},
    {"id": "i004", "name": "카카오 고객센터", "category": "IT/전자", "subcategory": "플랫폼", "tel": "1577-3344", "ars": "", "hours": "평일 09:00~18:00", "official": True},
    {"id": "i005", "name": "네이버 고객센터", "category": "IT/전자", "subcategory": "플랫폼", "tel": "1588-3820", "ars": "", "hours": "평일 09:00~18:00", "official": True},
    {"id": "i006", "name": "당근마켓", "category": "IT/전자", "subcategory": "플랫폼", "tel": "1670-2910", "ars": "", "hours": "평일 09:00~18:00", "official": True},
    {"id": "i007", "name": "배달의민족", "category": "IT/전자", "subcategory": "플랫폼", "tel": "1670-0862", "ars": "", "hours": "24시간", "official": True},
    {"id": "i008", "name": "요기요", "category": "IT/전자", "subcategory": "플랫폼", "tel": "1644-0760", "ars": "", "hours": "평일 09:00~18:00", "official": True},
    {"id": "i009", "name": "쏘카", "category": "IT/전자", "subcategory": "모빌리티", "tel": "1661-6195", "ars": "", "hours": "24시간", "official": True},
    {"id": "i010", "name": "카카오T(택시)", "category": "IT/전자", "subcategory": "모빌리티", "tel": "1833-3114", "ars": "", "hours": "24시간", "official": True},
]

delivery = [
    {"id": "d001", "name": "CJ대한통운", "category": "택배/물류", "subcategory": "택배", "tel": "1588-1255", "ars": "1→배송조회/2→분실", "hours": "평일 09:00~18:00", "official": True},
    {"id": "d002", "name": "한진택배", "category": "택배/물류", "subcategory": "택배", "tel": "1588-0011", "ars": "", "hours": "평일 09:00~18:00", "official": True},
    {"id": "d003", "name": "롯데택배", "category": "택배/물류", "subcategory": "택배", "tel": "1588-2121", "ars": "", "hours": "평일 09:00~18:00", "official": True},
    {"id": "d004", "name": "로젠택배", "category": "택배/물류", "subcategory": "택배", "tel": "1588-9988", "ars": "", "hours": "평일 09:00~18:00", "official": True},
    {"id": "d005", "name": "우체국택배", "category": "택배/물류", "subcategory": "택배", "tel": "1588-1300", "ars": "", "hours": "평일 09:00~18:00", "official": True},
    {"id": "d006", "name": "쿠팡로켓배송(쿠팡)", "category": "택배/물류", "subcategory": "로켓배송", "tel": "1577-7011", "ars": "2→배송문의", "hours": "24시간", "official": True},
]

shopping = [
    {"id": "s001", "name": "쿠팡 고객센터", "category": "쇼핑", "subcategory": "이커머스", "tel": "1577-7011", "ars": "1→주문/2→배송/3→반품", "hours": "24시간", "official": True},
    {"id": "s002", "name": "11번가", "category": "쇼핑", "subcategory": "이커머스", "tel": "1566-1155", "ars": "", "hours": "평일 09:00~18:00", "official": True},
    {"id": "s003", "name": "G마켓/옥션", "category": "쇼핑", "subcategory": "이커머스", "tel": "1566-5701", "ars": "", "hours": "평일 09:00~18:00", "official": True},
    {"id": "s004", "name": "SSG닷컴", "category": "쇼핑", "subcategory": "이커머스", "tel": "1644-0055", "ars": "", "hours": "평일 09:00~18:00", "official": True},
    {"id": "s005", "name": "롯데온", "category": "쇼핑", "subcategory": "이커머스", "tel": "1588-2110", "ars": "", "hours": "평일 09:00~18:00", "official": True},
    {"id": "s006", "name": "무신사", "category": "쇼핑", "subcategory": "패션", "tel": "1877-0553", "ars": "", "hours": "평일 09:00~18:00", "official": True},
    {"id": "s007", "name": "오늘의집", "category": "쇼핑", "subcategory": "인테리어", "tel": "1644-8755", "ars": "", "hours": "평일 09:00~18:00", "official": True},
    {"id": "s008", "name": "마켓컬리", "category": "쇼핑", "subcategory": "식품", "tel": "1644-1107", "ars": "", "hours": "24시간", "official": True},
]

airline = [
    {"id": "a001", "name": "대한항공", "category": "항공/여행", "subcategory": "항공", "tel": "1588-2001", "ars": "1→예약/2→마일리지", "hours": "24시간", "official": True},
    {"id": "a002", "name": "아시아나항공", "category": "항공/여행", "subcategory": "항공", "tel": "1588-8000", "ars": "", "hours": "24시간", "official": True},
    {"id": "a003", "name": "제주항공", "category": "항공/여행", "subcategory": "항공", "tel": "1599-1500", "ars": "", "hours": "24시간", "official": True},
    {"id": "a004", "name": "진에어", "category": "항공/여행", "subcategory": "항공", "tel": "1600-6200", "ars": "", "hours": "24시간", "official": True},
    {"id": "a005", "name": "티웨이항공", "category": "항공/여행", "subcategory": "항공", "tel": "1688-8686", "ars": "", "hours": "24시간", "official": True},
    {"id": "a006", "name": "에어서울", "category": "항공/여행", "subcategory": "항공", "tel": "1800-8100", "ars": "", "hours": "24시간", "official": True},
    {"id": "a007", "name": "에어부산", "category": "항공/여행", "subcategory": "항공", "tel": "1666-3060", "ars": "", "hours": "24시간", "official": True},
    {"id": "a008", "name": "여기어때", "category": "항공/여행", "subcategory": "숙박", "tel": "1670-8208", "ars": "", "hours": "24시간", "official": True},
    {"id": "a009", "name": "야놀자", "category": "항공/여행", "subcategory": "숙박", "tel": "1800-2499", "ars": "", "hours": "24시간", "official": True},
    {"id": "a010", "name": "에어비앤비 한국", "category": "항공/여행", "subcategory": "숙박", "tel": "02-6022-2499", "ars": "", "hours": "24시간", "official": True},
]

auto = [
    {"id": "au001", "name": "현대자동차 서비스", "category": "자동차", "subcategory": "국산차", "tel": "1588-8000", "ars": "1→긴급출동/2→서비스", "hours": "24시간(긴급)", "official": True},
    {"id": "au002", "name": "기아 서비스", "category": "자동차", "subcategory": "국산차", "tel": "1833-4000", "ars": "", "hours": "24시간(긴급)", "official": True},
    {"id": "au003", "name": "KG모빌리티(쌍용)", "category": "자동차", "subcategory": "국산차", "tel": "1588-0100", "ars": "", "hours": "24시간(긴급)", "official": True},
    {"id": "au004", "name": "BMW코리아", "category": "자동차", "subcategory": "수입차", "tel": "1600-3000", "ars": "", "hours": "평일 09:00~18:00", "official": True},
    {"id": "au005", "name": "메르세데스-벤츠코리아", "category": "자동차", "subcategory": "수입차", "tel": "1800-1800", "ars": "", "hours": "24시간", "official": True},
    {"id": "au006", "name": "아우디코리아", "category": "자동차", "subcategory": "수입차", "tel": "080-799-8500", "ars": "", "hours": "평일 09:00~18:00", "official": True},
    {"id": "au007", "name": "테슬라코리아", "category": "자동차", "subcategory": "수입차", "tel": "080-780-6780", "ars": "", "hours": "평일 09:00~18:00", "official": True},
    {"id": "au008", "name": "도요타코리아", "category": "자동차", "subcategory": "수입차", "tel": "1588-0500", "ars": "", "hours": "평일 09:00~18:00", "official": True},
    {"id": "au009", "name": "볼보자동차코리아", "category": "자동차", "subcategory": "수입차", "tel": "080-600-6060", "ars": "", "hours": "평일 09:00~18:00", "official": True},
    {"id": "au010", "name": "한국GM 쉐보레", "category": "자동차", "subcategory": "국산차", "tel": "1588-1600", "ars": "", "hours": "24시간(긴급)", "official": True},
]

foreign = [
    {"id": "fo001", "name": "P&G코리아", "category": "외국계기업", "subcategory": "생활용품", "tel": "080-023-5454", "ars": "", "hours": "평일 09:00~18:00", "official": True},
    {"id": "fo002", "name": "존슨앤드존슨 한국", "category": "외국계기업", "subcategory": "의료/생활", "tel": "080-023-8200", "ars": "", "hours": "평일 09:00~18:00", "official": True},
    {"id": "fo003", "name": "한국 3M", "category": "외국계기업", "subcategory": "산업/생활", "tel": "1544-3002", "ars": "", "hours": "평일 09:00~18:00", "official": True},
    {"id": "fo004", "name": "마이크로소프트코리아", "category": "외국계기업", "subcategory": "IT", "tel": "02-531-4500", "ars": "", "hours": "평일 09:00~18:00", "official": True},
    {"id": "fo005", "name": "구글코리아", "category": "외국계기업", "subcategory": "IT", "tel": "1600-1531", "ars": "", "hours": "평일 09:00~18:00", "official": True},
    {"id": "fo006", "name": "아마존웹서비스코리아", "category": "외국계기업", "subcategory": "IT", "tel": "1599-3528", "ars": "", "hours": "24시간", "official": True},
    {"id": "fo007", "name": "코카콜라음료", "category": "외국계기업", "subcategory": "식음료", "tel": "080-026-5656", "ars": "", "hours": "평일 09:00~18:00", "official": True},
    {"id": "fo008", "name": "한국 네슬레", "category": "외국계기업", "subcategory": "식음료", "tel": "080-022-2333", "ars": "", "hours": "평일 09:00~18:00", "official": True},
    {"id": "fo009", "name": "한국 크래프트하인즈", "category": "외국계기업", "subcategory": "식품", "tel": "02-3459-5800", "ars": "", "hours": "평일 09:00~18:00", "official": True},
    {"id": "fo010", "name": "나이키코리아", "category": "외국계기업", "subcategory": "스포츠/패션", "tel": "080-022-0182", "ars": "", "hours": "평일 09:00~18:00", "official": True},
    {"id": "fo011", "name": "아디다스코리아", "category": "외국계기업", "subcategory": "스포츠/패션", "tel": "080-022-0604", "ars": "", "hours": "평일 09:00~18:00", "official": True},
    {"id": "fo012", "name": "이케아코리아", "category": "외국계기업", "subcategory": "가구/인테리어", "tel": "1670-4532", "ars": "", "hours": "평일 09:00~18:00", "official": True},
    {"id": "fo013", "name": "유니클로코리아", "category": "외국계기업", "subcategory": "패션", "tel": "080-022-0700", "ars": "", "hours": "평일 09:00~18:00", "official": True},
    {"id": "fo014", "name": "자라코리아", "category": "외국계기업", "subcategory": "패션", "tel": "1661-2016", "ars": "", "hours": "평일 09:00~18:00", "official": True},
    {"id": "fo015", "name": "H&M코리아", "category": "외국계기업", "subcategory": "패션", "tel": "080-022-1990", "ars": "", "hours": "평일 09:00~18:00", "official": True},
    {"id": "fo016", "name": "맥도날드코리아", "category": "외국계기업", "subcategory": "외식", "tel": "1600-5252", "ars": "", "hours": "24시간", "official": True},
    {"id": "fo017", "name": "버거킹코리아", "category": "외국계기업", "subcategory": "외식", "tel": "1599-0100", "ars": "", "hours": "평일 09:00~18:00", "official": True},
    {"id": "fo018", "name": "KFC코리아", "category": "외국계기업", "subcategory": "외식", "tel": "1600-3654", "ars": "", "hours": "평일 09:00~18:00", "official": True},
    {"id": "fo019", "name": "스타벅스코리아", "category": "외국계기업", "subcategory": "외식", "tel": "1522-3232", "ars": "", "hours": "평일 07:00~22:00", "official": True},
]

retail = [
    {"id": "r001", "name": "이마트", "category": "유통", "subcategory": "대형마트", "tel": "1588-1234", "ars": "", "hours": "평일 09:00~18:00", "official": True},
    {"id": "r002", "name": "롯데마트", "category": "유통", "subcategory": "대형마트", "tel": "1668-0110", "ars": "", "hours": "평일 09:00~18:00", "official": True},
    {"id": "r003", "name": "홈플러스", "category": "유통", "subcategory": "대형마트", "tel": "1588-0030", "ars": "", "hours": "평일 09:00~18:00", "official": True},
    {"id": "r004", "name": "코스트코코리아", "category": "유통", "subcategory": "대형마트", "tel": "1899-9900", "ars": "", "hours": "평일 09:00~18:00", "official": True},
    {"id": "r005", "name": "GS25", "category": "유통", "subcategory": "편의점", "tel": "080-900-0001", "ars": "", "hours": "24시간", "official": True},
    {"id": "r006", "name": "CU편의점", "category": "유통", "subcategory": "편의점", "tel": "1577-9093", "ars": "", "hours": "평일 09:00~18:00", "official": True},
    {"id": "r007", "name": "세븐일레븐", "category": "유통", "subcategory": "편의점", "tel": "1588-7711", "ars": "", "hours": "평일 09:00~18:00", "official": True},
    {"id": "r008", "name": "다이소", "category": "유통", "subcategory": "생활용품", "tel": "1800-8900", "ars": "", "hours": "평일 09:00~18:00", "official": True},
    {"id": "r009", "name": "올리브영", "category": "유통", "subcategory": "헬스/뷰티", "tel": "1599-8000", "ars": "", "hours": "평일 09:00~18:00", "official": True},
]

food = [
    {"id": "fn001", "name": "CJ제일제당", "category": "식품", "subcategory": "식품제조", "tel": "1577-2595", "ars": "", "hours": "평일 09:00~18:00", "official": True},
    {"id": "fn002", "name": "농심", "category": "식품", "subcategory": "식품제조", "tel": "080-023-6565", "ars": "", "hours": "평일 09:00~18:00", "official": True},
    {"id": "fn003", "name": "오뚜기", "category": "식품", "subcategory": "식품제조", "tel": "080-022-7751", "ars": "", "hours": "평일 09:00~18:00", "official": True},
    {"id": "fn004", "name": "동원F&B", "category": "식품", "subcategory": "식품제조", "tel": "1588-3252", "ars": "", "hours": "평일 09:00~18:00", "official": True},
    {"id": "fn005", "name": "롯데웰푸드", "category": "식품", "subcategory": "식품제조", "tel": "080-023-9901", "ars": "", "hours": "평일 09:00~18:00", "official": True},
]

all_contacts = emergency + government + public_org + telecom + finance + it_electronics + delivery + shopping + airline + auto + foreign + retail + food

print(f"1단계 총 {len(all_contacts)}개 연락처 수집 완료")

cats = Counter(c['category'] for c in all_contacts)
for cat, count in sorted(cats.items()):
    print(f"  {cat}: {count}개")

with open('/Users/toctgx/golfmap-contacts/contacts_v1.json', 'w', encoding='utf-8') as f:
    json.dump(all_contacts, f, ensure_ascii=False, indent=2)

print("\n✅ contacts_v1.json 저장 완료")
