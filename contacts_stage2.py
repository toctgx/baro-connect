import json

# 2단계 대량 연락처 데이터
# 공공기관 확장 + 지자체 + 대기업/중견기업 + 외국계 확장

stage2 = []

# ── 지자체 광역시/도 ──
local_gov = [
    # 서울
    {"id": "lg001", "name": "서울시청", "category": "지자체", "subcategory": "서울", "tel": "02-120", "ars": "", "hours": "24시간", "official": True},
    {"id": "lg002", "name": "서울 강남구청", "category": "지자체", "subcategory": "서울", "tel": "02-3423-5114", "ars": "", "hours": "평일 09:00~18:00", "official": True},
    {"id": "lg003", "name": "서울 강서구청", "category": "지자체", "subcategory": "서울", "tel": "02-2600-6114", "ars": "", "hours": "평일 09:00~18:00", "official": True},
    {"id": "lg004", "name": "서울 강북구청", "category": "지자체", "subcategory": "서울", "tel": "02-901-6114", "ars": "", "hours": "평일 09:00~18:00", "official": True},
    {"id": "lg005", "name": "서울 강동구청", "category": "지자체", "subcategory": "서울", "tel": "02-3425-114", "ars": "", "hours": "평일 09:00~18:00", "official": True},
    {"id": "lg006", "name": "서울 마포구청", "category": "지자체", "subcategory": "서울", "tel": "02-3153-8000", "ars": "", "hours": "평일 09:00~18:00", "official": True},
    {"id": "lg007", "name": "서울 송파구청", "category": "지자체", "subcategory": "서울", "tel": "02-2147-2000", "ars": "", "hours": "평일 09:00~18:00", "official": True},
    {"id": "lg008", "name": "서울 서초구청", "category": "지자체", "subcategory": "서울", "tel": "02-2155-6114", "ars": "", "hours": "평일 09:00~18:00", "official": True},
    {"id": "lg009", "name": "서울 용산구청", "category": "지자체", "subcategory": "서울", "tel": "02-2199-6114", "ars": "", "hours": "평일 09:00~18:00", "official": True},
    {"id": "lg010", "name": "서울 종로구청", "category": "지자체", "subcategory": "서울", "tel": "02-2148-1114", "ars": "", "hours": "평일 09:00~18:00", "official": True},
    {"id": "lg011", "name": "서울 중구청", "category": "지자체", "subcategory": "서울", "tel": "02-3396-4114", "ars": "", "hours": "평일 09:00~18:00", "official": True},
    {"id": "lg012", "name": "서울 성동구청", "category": "지자체", "subcategory": "서울", "tel": "02-2286-5114", "ars": "", "hours": "평일 09:00~18:00", "official": True},
    {"id": "lg013", "name": "서울 광진구청", "category": "지자체", "subcategory": "서울", "tel": "02-450-7114", "ars": "", "hours": "평일 09:00~18:00", "official": True},
    {"id": "lg014", "name": "서울 동대문구청", "category": "지자체", "subcategory": "서울", "tel": "02-2127-4114", "ars": "", "hours": "평일 09:00~18:00", "official": True},
    {"id": "lg015", "name": "서울 중랑구청", "category": "지자체", "subcategory": "서울", "tel": "02-2094-0114", "ars": "", "hours": "평일 09:00~18:00", "official": True},
    {"id": "lg016", "name": "서울 성북구청", "category": "지자체", "subcategory": "서울", "tel": "02-2241-2114", "ars": "", "hours": "평일 09:00~18:00", "official": True},
    {"id": "lg017", "name": "서울 도봉구청", "category": "지자체", "subcategory": "서울", "tel": "02-2091-2114", "ars": "", "hours": "평일 09:00~18:00", "official": True},
    {"id": "lg018", "name": "서울 노원구청", "category": "지자체", "subcategory": "서울", "tel": "02-2116-3114", "ars": "", "hours": "평일 09:00~18:00", "official": True},
    {"id": "lg019", "name": "서울 은평구청", "category": "지자체", "subcategory": "서울", "tel": "02-351-6114", "ars": "", "hours": "평일 09:00~18:00", "official": True},
    {"id": "lg020", "name": "서울 서대문구청", "category": "지자체", "subcategory": "서울", "tel": "02-330-1114", "ars": "", "hours": "평일 09:00~18:00", "official": True},
    {"id": "lg021", "name": "서울 양천구청", "category": "지자체", "subcategory": "서울", "tel": "02-2620-5000", "ars": "", "hours": "평일 09:00~18:00", "official": True},
    {"id": "lg022", "name": "서울 구로구청", "category": "지자체", "subcategory": "서울", "tel": "02-860-2114", "ars": "", "hours": "평일 09:00~18:00", "official": True},
    {"id": "lg023", "name": "서울 금천구청", "category": "지자체", "subcategory": "서울", "tel": "02-2627-1000", "ars": "", "hours": "평일 09:00~18:00", "official": True},
    {"id": "lg024", "name": "서울 영등포구청", "category": "지자체", "subcategory": "서울", "tel": "02-2670-3114", "ars": "", "hours": "평일 09:00~18:00", "official": True},
    {"id": "lg025", "name": "서울 동작구청", "category": "지자체", "subcategory": "서울", "tel": "02-820-9114", "ars": "", "hours": "평일 09:00~18:00", "official": True},
    {"id": "lg026", "name": "서울 관악구청", "category": "지자체", "subcategory": "서울", "tel": "02-879-5114", "ars": "", "hours": "평일 09:00~18:00", "official": True},
    # 경기
    {"id": "lg027", "name": "경기도청", "category": "지자체", "subcategory": "경기", "tel": "031-120", "ars": "", "hours": "평일 09:00~18:00", "official": True},
    {"id": "lg028", "name": "수원시청", "category": "지자체", "subcategory": "경기", "tel": "031-228-2114", "ars": "", "hours": "평일 09:00~18:00", "official": True},
    {"id": "lg029", "name": "성남시청", "category": "지자체", "subcategory": "경기", "tel": "031-729-2114", "ars": "", "hours": "평일 09:00~18:00", "official": True},
    {"id": "lg030", "name": "고양시청", "category": "지자체", "subcategory": "경기", "tel": "031-909-9114", "ars": "", "hours": "평일 09:00~18:00", "official": True},
    {"id": "lg031", "name": "용인시청", "category": "지자체", "subcategory": "경기", "tel": "031-324-2114", "ars": "", "hours": "평일 09:00~18:00", "official": True},
    {"id": "lg032", "name": "부천시청", "category": "지자체", "subcategory": "경기", "tel": "032-625-2114", "ars": "", "hours": "평일 09:00~18:00", "official": True},
    {"id": "lg033", "name": "안산시청", "category": "지자체", "subcategory": "경기", "tel": "031-481-2114", "ars": "", "hours": "평일 09:00~18:00", "official": True},
    {"id": "lg034", "name": "안양시청", "category": "지자체", "subcategory": "경기", "tel": "031-8045-2114", "ars": "", "hours": "평일 09:00~18:00", "official": True},
    {"id": "lg035", "name": "남양주시청", "category": "지자체", "subcategory": "경기", "tel": "031-590-2000", "ars": "", "hours": "평일 09:00~18:00", "official": True},
    {"id": "lg036", "name": "화성시청", "category": "지자체", "subcategory": "경기", "tel": "031-369-2114", "ars": "", "hours": "평일 09:00~18:00", "official": True},
    # 인천
    {"id": "lg037", "name": "인천시청", "category": "지자체", "subcategory": "인천", "tel": "032-120", "ars": "", "hours": "평일 09:00~18:00", "official": True},
    {"id": "lg038", "name": "인천 남동구청", "category": "지자체", "subcategory": "인천", "tel": "032-453-2114", "ars": "", "hours": "평일 09:00~18:00", "official": True},
    {"id": "lg039", "name": "인천 부평구청", "category": "지자체", "subcategory": "인천", "tel": "032-509-6114", "ars": "", "hours": "평일 09:00~18:00", "official": True},
    # 부산
    {"id": "lg040", "name": "부산시청", "category": "지자체", "subcategory": "부산", "tel": "051-120", "ars": "", "hours": "평일 09:00~18:00", "official": True},
    {"id": "lg041", "name": "부산 해운대구청", "category": "지자체", "subcategory": "부산", "tel": "051-749-4000", "ars": "", "hours": "평일 09:00~18:00", "official": True},
    {"id": "lg042", "name": "부산 부산진구청", "category": "지자체", "subcategory": "부산", "tel": "051-605-4000", "ars": "", "hours": "평일 09:00~18:00", "official": True},
    # 대구
    {"id": "lg043", "name": "대구시청", "category": "지자체", "subcategory": "대구", "tel": "053-120", "ars": "", "hours": "평일 09:00~18:00", "official": True},
    # 대전
    {"id": "lg044", "name": "대전시청", "category": "지자체", "subcategory": "대전", "tel": "042-120", "ars": "", "hours": "평일 09:00~18:00", "official": True},
    # 광주
    {"id": "lg045", "name": "광주시청", "category": "지자체", "subcategory": "광주", "tel": "062-120", "ars": "", "hours": "평일 09:00~18:00", "official": True},
    # 울산
    {"id": "lg046", "name": "울산시청", "category": "지자체", "subcategory": "울산", "tel": "052-120", "ars": "", "hours": "평일 09:00~18:00", "official": True},
    # 세종
    {"id": "lg047", "name": "세종시청", "category": "지자체", "subcategory": "세종", "tel": "044-300-2114", "ars": "", "hours": "평일 09:00~18:00", "official": True},
    # 강원
    {"id": "lg048", "name": "강원도청", "category": "지자체", "subcategory": "강원", "tel": "033-120", "ars": "", "hours": "평일 09:00~18:00", "official": True},
    {"id": "lg049", "name": "춘천시청", "category": "지자체", "subcategory": "강원", "tel": "033-250-3000", "ars": "", "hours": "평일 09:00~18:00", "official": True},
    # 충북
    {"id": "lg050", "name": "충청북도청", "category": "지자체", "subcategory": "충북", "tel": "043-220-2114", "ars": "", "hours": "평일 09:00~18:00", "official": True},
    {"id": "lg051", "name": "청주시청", "category": "지자체", "subcategory": "충북", "tel": "043-201-1114", "ars": "", "hours": "평일 09:00~18:00", "official": True},
    # 충남
    {"id": "lg052", "name": "충청남도청", "category": "지자체", "subcategory": "충남", "tel": "041-635-2114", "ars": "", "hours": "평일 09:00~18:00", "official": True},
    {"id": "lg053", "name": "천안시청", "category": "지자체", "subcategory": "충남", "tel": "041-521-2114", "ars": "", "hours": "평일 09:00~18:00", "official": True},
    # 전북
    {"id": "lg054", "name": "전라북도청", "category": "지자체", "subcategory": "전북", "tel": "063-280-2114", "ars": "", "hours": "평일 09:00~18:00", "official": True},
    {"id": "lg055", "name": "전주시청", "category": "지자체", "subcategory": "전북", "tel": "063-281-2114", "ars": "", "hours": "평일 09:00~18:00", "official": True},
    # 전남
    {"id": "lg056", "name": "전라남도청", "category": "지자체", "subcategory": "전남", "tel": "061-286-2114", "ars": "", "hours": "평일 09:00~18:00", "official": True},
    # 경북
    {"id": "lg057", "name": "경상북도청", "category": "지자체", "subcategory": "경북", "tel": "054-880-2114", "ars": "", "hours": "평일 09:00~18:00", "official": True},
    {"id": "lg058", "name": "포항시청", "category": "지자체", "subcategory": "경북", "tel": "054-245-6114", "ars": "", "hours": "평일 09:00~18:00", "official": True},
    # 경남
    {"id": "lg059", "name": "경상남도청", "category": "지자체", "subcategory": "경남", "tel": "055-211-2114", "ars": "", "hours": "평일 09:00~18:00", "official": True},
    {"id": "lg060", "name": "창원시청", "category": "지자체", "subcategory": "경남", "tel": "055-225-2114", "ars": "", "hours": "평일 09:00~18:00", "official": True},
    # 제주
    {"id": "lg061", "name": "제주도청", "category": "지자체", "subcategory": "제주", "tel": "064-710-3114", "ars": "", "hours": "평일 09:00~18:00", "official": True},
    {"id": "lg062", "name": "제주시청", "category": "지자체", "subcategory": "제주", "tel": "064-728-2114", "ars": "", "hours": "평일 09:00~18:00", "official": True},
]

# ── 의료/건강 ──
medical = [
    {"id": "m001", "name": "서울대학교병원", "category": "의료", "subcategory": "상급종합병원", "tel": "1588-5700", "ars": "", "hours": "평일 09:00~17:00", "official": True},
    {"id": "m002", "name": "삼성서울병원", "category": "의료", "subcategory": "상급종합병원", "tel": "1599-3114", "ars": "", "hours": "평일 09:00~17:00", "official": True},
    {"id": "m003", "name": "세브란스병원", "category": "의료", "subcategory": "상급종합병원", "tel": "1599-1004", "ars": "", "hours": "평일 09:00~17:00", "official": True},
    {"id": "m004", "name": "서울아산병원", "category": "의료", "subcategory": "상급종합병원", "tel": "1688-7575", "ars": "", "hours": "평일 09:00~17:00", "official": True},
    {"id": "m005", "name": "가톨릭대 서울성모병원", "category": "의료", "subcategory": "상급종합병원", "tel": "1588-1511", "ars": "", "hours": "평일 09:00~17:00", "official": True},
    {"id": "m006", "name": "질병관리청 콜센터", "category": "의료", "subcategory": "공공의료", "tel": "1339", "ars": "", "hours": "24시간", "official": True},
    {"id": "m007", "name": "정신건강위기상담", "category": "의료", "subcategory": "상담", "tel": "1577-0199", "ars": "", "hours": "24시간", "official": True},
    {"id": "m008", "name": "응급의료정보센터", "category": "의료", "subcategory": "응급", "tel": "1339", "ars": "", "hours": "24시간", "official": True},
    {"id": "m009", "name": "한국희귀필수의약품센터", "category": "의료", "subcategory": "의약품", "tel": "02-508-7316", "ars": "", "hours": "평일 09:00~18:00", "official": True},
    {"id": "m010", "name": "대한적십자사", "category": "의료", "subcategory": "헌혈/봉사", "tel": "1365", "ars": "", "hours": "24시간", "official": True},
]

# ── 에너지/유틸리티 ──
energy = [
    {"id": "en001", "name": "한전 전기고장신고", "category": "에너지", "subcategory": "전기", "tel": "123", "ars": "1→고장신고", "hours": "24시간", "official": True},
    {"id": "en002", "name": "도시가스 긴급신고", "category": "에너지", "subcategory": "가스", "tel": "1544-4500", "ars": "", "hours": "24시간", "official": True},
    {"id": "en003", "name": "서울도시가스", "category": "에너지", "subcategory": "가스", "tel": "1544-0011", "ars": "", "hours": "24시간", "official": True},
    {"id": "en004", "name": "SK에너지 주유소", "category": "에너지", "subcategory": "주유", "tel": "1599-0015", "ars": "", "hours": "평일 09:00~18:00", "official": True},
    {"id": "en005", "name": "GS칼텍스", "category": "에너지", "subcategory": "주유", "tel": "1588-1588", "ars": "", "hours": "평일 09:00~18:00", "official": True},
]

# ── 교육 ──
education = [
    {"id": "ed001", "name": "교육부 민원콜센터", "category": "교육", "subcategory": "정부", "tel": "02-6222-6060", "ars": "", "hours": "평일 09:00~18:00", "official": True},
    {"id": "ed002", "name": "한국교육학술정보원(KERIS)", "category": "교육", "subcategory": "교육정보", "tel": "1544-0107", "ars": "", "hours": "평일 09:00~18:00", "official": True},
    {"id": "ed003", "name": "수능접수/성적 한국교육과정평가원", "category": "교육", "subcategory": "수능", "tel": "1566-0990", "ars": "", "hours": "평일 09:00~18:00", "official": True},
    {"id": "ed004", "name": "대학수학능력시험 콜센터", "category": "교육", "subcategory": "수능", "tel": "1588-1288", "ars": "", "hours": "평일 09:00~18:00", "official": True},
    {"id": "ed005", "name": "국가평생교육진흥원", "category": "교육", "subcategory": "평생교육", "tel": "1588-6248", "ars": "", "hours": "평일 09:00~18:00", "official": True},
    {"id": "ed006", "name": "학점은행제", "category": "교육", "subcategory": "학점인정", "tel": "1600-0200", "ars": "", "hours": "평일 09:00~18:00", "official": True},
    {"id": "ed007", "name": "EBS", "category": "교육", "subcategory": "교육방송", "tel": "1588-1580", "ars": "", "hours": "평일 09:00~18:00", "official": True},
]

# ── 법률/법무 ──
legal = [
    {"id": "le001", "name": "대한법률구조공단", "category": "법률", "subcategory": "법률구조", "tel": "132", "ars": "", "hours": "평일 09:00~18:00", "official": True},
    {"id": "le002", "name": "법원 민원콜센터", "category": "법률", "subcategory": "법원", "tel": "1670-1992", "ars": "", "hours": "평일 09:00~18:00", "official": True},
    {"id": "le003", "name": "헌법재판소", "category": "법률", "subcategory": "헌법재판", "tel": "02-708-3456", "ars": "", "hours": "평일 09:00~18:00", "official": True},
    {"id": "le004", "name": "검찰청 범죄신고", "category": "법률", "subcategory": "검찰", "tel": "1301", "ars": "", "hours": "24시간", "official": True},
    {"id": "le005", "name": "법무부 법률상담", "category": "법률", "subcategory": "법무", "tel": "02-2110-3000", "ars": "", "hours": "평일 09:00~18:00", "official": True},
]

# ── 대기업 확장 ──
conglomerate = [
    # 삼성그룹
    {"id": "cg001", "name": "삼성전자 (MX/가전)", "category": "대기업", "subcategory": "삼성그룹", "tel": "1588-3366", "ars": "1→모바일/2→TV/3→가전/4→PC", "hours": "평일 09:00~18:00", "official": True},
    {"id": "cg002", "name": "삼성생명", "category": "대기업", "subcategory": "삼성그룹", "tel": "1588-3114", "ars": "", "hours": "평일 09:00~18:00", "official": True},
    {"id": "cg003", "name": "삼성화재", "category": "대기업", "subcategory": "삼성그룹", "tel": "1588-5114", "ars": "1→사고접수", "hours": "24시간(사고)", "official": True},
    {"id": "cg004", "name": "삼성카드", "category": "대기업", "subcategory": "삼성그룹", "tel": "1588-8900", "ars": "분실→1번", "hours": "24시간", "official": True},
    {"id": "cg005", "name": "삼성증권", "category": "대기업", "subcategory": "삼성그룹", "tel": "1588-2323", "ars": "", "hours": "평일 09:00~18:00", "official": True},
    {"id": "cg006", "name": "이마트/SSG", "category": "대기업", "subcategory": "신세계그룹", "tel": "1588-1234", "ars": "", "hours": "평일 09:00~18:00", "official": True},
    {"id": "cg007", "name": "신세계백화점", "category": "대기업", "subcategory": "신세계그룹", "tel": "1588-1234", "ars": "", "hours": "평일 09:00~18:00", "official": True},
    # 현대그룹
    {"id": "cg008", "name": "현대자동차", "category": "대기업", "subcategory": "현대그룹", "tel": "1588-8000", "ars": "1→긴급출동/2→AS", "hours": "24시간(긴급)", "official": True},
    {"id": "cg009", "name": "현대건설", "category": "대기업", "subcategory": "현대그룹", "tel": "1544-5000", "ars": "", "hours": "평일 09:00~18:00", "official": True},
    {"id": "cg010", "name": "현대백화점", "category": "대기업", "subcategory": "현대그룹", "tel": "1577-6000", "ars": "", "hours": "평일 09:00~18:00", "official": True},
    {"id": "cg011", "name": "현대홈쇼핑", "category": "대기업", "subcategory": "현대그룹", "tel": "1588-1100", "ars": "", "hours": "24시간", "official": True},
    # LG그룹
    {"id": "cg012", "name": "LG전자 서비스", "category": "대기업", "subcategory": "LG그룹", "tel": "1544-7777", "ars": "1→가전/2→모바일/3→TV", "hours": "평일 09:00~18:00", "official": True},
    {"id": "cg013", "name": "LG생활건강", "category": "대기업", "subcategory": "LG그룹", "tel": "080-023-8800", "ars": "", "hours": "평일 09:00~18:00", "official": True},
    {"id": "cg014", "name": "LG유플러스", "category": "대기업", "subcategory": "LG그룹", "tel": "101", "ars": "0→상담원", "hours": "24시간", "official": True},
    # 롯데그룹
    {"id": "cg015", "name": "롯데백화점", "category": "대기업", "subcategory": "롯데그룹", "tel": "1588-3344", "ars": "", "hours": "평일 09:00~18:00", "official": True},
    {"id": "cg016", "name": "롯데마트", "category": "대기업", "subcategory": "롯데그룹", "tel": "1668-0110", "ars": "", "hours": "평일 09:00~18:00", "official": True},
    {"id": "cg017", "name": "롯데카드", "category": "대기업", "subcategory": "롯데그룹", "tel": "1588-8100", "ars": "분실→1번", "hours": "24시간(분실)", "official": True},
    {"id": "cg018", "name": "롯데렌탈", "category": "대기업", "subcategory": "롯데그룹", "tel": "1588-1230", "ars": "", "hours": "평일 09:00~18:00", "official": True},
    # SK그룹
    {"id": "cg019", "name": "SK텔레콤", "category": "대기업", "subcategory": "SK그룹", "tel": "1599-0011", "ars": "0→상담원", "hours": "24시간", "official": True},
    {"id": "cg020", "name": "SK하이닉스", "category": "대기업", "subcategory": "SK그룹", "tel": "031-8086-0001", "ars": "", "hours": "평일 09:00~18:00", "official": True},
    {"id": "cg021", "name": "SK에너지", "category": "대기업", "subcategory": "SK그룹", "tel": "1599-0015", "ars": "", "hours": "평일 09:00~18:00", "official": True},
    # GS그룹
    {"id": "cg022", "name": "GS25 편의점", "category": "대기업", "subcategory": "GS그룹", "tel": "080-900-0001", "ars": "", "hours": "24시간", "official": True},
    {"id": "cg023", "name": "GS홈쇼핑", "category": "대기업", "subcategory": "GS그룹", "tel": "1588-1588", "ars": "", "hours": "24시간", "official": True},
    {"id": "cg024", "name": "GS칼텍스", "category": "대기업", "subcategory": "GS그룹", "tel": "1588-1588", "ars": "", "hours": "평일 09:00~18:00", "official": True},
    # CJ그룹
    {"id": "cg025", "name": "CJ제일제당", "category": "대기업", "subcategory": "CJ그룹", "tel": "1577-2595", "ars": "", "hours": "평일 09:00~18:00", "official": True},
    {"id": "cg026", "name": "CJ대한통운", "category": "대기업", "subcategory": "CJ그룹", "tel": "1588-1255", "ars": "1→배송조회", "hours": "평일 09:00~18:00", "official": True},
    {"id": "cg027", "name": "CJ ENM(올리브영 포함)", "category": "대기업", "subcategory": "CJ그룹", "tel": "1577-1000", "ars": "", "hours": "평일 09:00~18:00", "official": True},
    {"id": "cg028", "name": "CJ CGV", "category": "대기업", "subcategory": "CJ그룹", "tel": "1544-1122", "ars": "", "hours": "24시간", "official": True},
    # 포스코/제철
    {"id": "cg029", "name": "포스코 고객지원", "category": "대기업", "subcategory": "포스코그룹", "tel": "054-220-0114", "ars": "", "hours": "평일 09:00~18:00", "official": True},
    # KT그룹
    {"id": "cg030", "name": "KT 통신", "category": "대기업", "subcategory": "KT그룹", "tel": "100", "ars": "0→상담원", "hours": "24시간", "official": True},
    {"id": "cg031", "name": "KT스카이라이프", "category": "대기업", "subcategory": "KT그룹", "tel": "1588-7200", "ars": "", "hours": "24시간", "official": True},
]

# ── 외국계 기업 확장 ──
foreign_ext = [
    # 자동차
    {"id": "fe001", "name": "폭스바겐코리아", "category": "외국계기업", "subcategory": "수입차", "tel": "080-222-1000", "ars": "", "hours": "평일 09:00~18:00", "official": True},
    {"id": "fe002", "name": "포르쉐코리아", "category": "외국계기업", "subcategory": "수입차", "tel": "02-2185-0911", "ars": "", "hours": "평일 09:00~18:00", "official": True},
    {"id": "fe003", "name": "재규어랜드로버코리아", "category": "외국계기업", "subcategory": "수입차", "tel": "080-600-5000", "ars": "", "hours": "평일 09:00~18:00", "official": True},
    {"id": "fe004", "name": "포드코리아", "category": "외국계기업", "subcategory": "수입차", "tel": "080-222-3673", "ars": "", "hours": "평일 09:00~18:00", "official": True},
    {"id": "fe005", "name": "링컨코리아", "category": "외국계기업", "subcategory": "수입차", "tel": "080-222-3673", "ars": "", "hours": "평일 09:00~18:00", "official": True},
    {"id": "fe006", "name": "렉서스코리아", "category": "외국계기업", "subcategory": "수입차", "tel": "080-600-5352", "ars": "", "hours": "평일 09:00~18:00", "official": True},
    {"id": "fe007", "name": "닛산코리아", "category": "외국계기업", "subcategory": "수입차", "tel": "080-600-5250", "ars": "", "hours": "평일 09:00~18:00", "official": True},
    {"id": "fe008", "name": "미니코리아", "category": "외국계기업", "subcategory": "수입차", "tel": "1600-3000", "ars": "", "hours": "평일 09:00~18:00", "official": True},
    # IT/플랫폼
    {"id": "fe009", "name": "넷플릭스 한국", "category": "외국계기업", "subcategory": "OTT", "tel": "080-803-0300", "ars": "", "hours": "24시간", "official": True},
    {"id": "fe010", "name": "유튜브(구글) 크리에이터", "category": "외국계기업", "subcategory": "플랫폼", "tel": "1600-1531", "ars": "", "hours": "평일 09:00~18:00", "official": True},
    {"id": "fe011", "name": "페이팔코리아", "category": "외국계기업", "subcategory": "핀테크", "tel": "00798-14-800-9551", "ars": "", "hours": "24시간", "official": True},
    # 생활용품/화장품
    {"id": "fe012", "name": "로레알코리아", "category": "외국계기업", "subcategory": "화장품", "tel": "080-023-1234", "ars": "", "hours": "평일 09:00~18:00", "official": True},
    {"id": "fe013", "name": "아모레퍼시픽", "category": "외국계기업", "subcategory": "화장품", "tel": "080-023-5454", "ars": "", "hours": "평일 09:00~18:00", "official": True},
    {"id": "fe014", "name": "에스티로더코리아", "category": "외국계기업", "subcategory": "화장품", "tel": "080-023-0023", "ars": "", "hours": "평일 09:00~18:00", "official": True},
    {"id": "fe015", "name": "샤넬코리아", "category": "외국계기업", "subcategory": "명품/화장품", "tel": "080-023-1234", "ars": "", "hours": "평일 10:00~18:00", "official": True},
    # 식음료
    {"id": "fe016", "name": "맥도날드코리아", "category": "외국계기업", "subcategory": "외식", "tel": "1600-5252", "ars": "", "hours": "24시간", "official": True},
    {"id": "fe017", "name": "피자헛코리아", "category": "외국계기업", "subcategory": "외식", "tel": "1588-5588", "ars": "", "hours": "24시간", "official": True},
    {"id": "fe018", "name": "도미노피자코리아", "category": "외국계기업", "subcategory": "외식", "tel": "1588-3082", "ars": "", "hours": "24시간", "official": True},
    {"id": "fe019", "name": "서브웨이코리아", "category": "외국계기업", "subcategory": "외식", "tel": "1899-7753", "ars": "", "hours": "평일 09:00~18:00", "official": True},
    {"id": "fe020", "name": "배스킨라빈스코리아", "category": "외국계기업", "subcategory": "외식", "tel": "1588-3258", "ars": "", "hours": "평일 09:00~18:00", "official": True},
    # 항공
    {"id": "fe021", "name": "델타항공 한국", "category": "외국계기업", "subcategory": "외항사", "tel": "02-754-1921", "ars": "", "hours": "24시간", "official": True},
    {"id": "fe022", "name": "유나이티드항공 한국", "category": "외국계기업", "subcategory": "외항사", "tel": "02-751-0300", "ars": "", "hours": "24시간", "official": True},
    {"id": "fe023", "name": "캐세이퍼시픽 한국", "category": "외국계기업", "subcategory": "외항사", "tel": "02-311-2800", "ars": "", "hours": "24시간", "official": True},
    {"id": "fe024", "name": "싱가포르항공 한국", "category": "외국계기업", "subcategory": "외항사", "tel": "02-755-1226", "ars": "", "hours": "평일 09:00~18:00", "official": True},
    {"id": "fe025", "name": "일본항공(JAL) 한국", "category": "외국계기업", "subcategory": "외항사", "tel": "02-757-1711", "ars": "", "hours": "평일 09:00~17:30", "official": True},
]

# ── 부동산/건설 ──
realestate = [
    {"id": "re001", "name": "직방 고객센터", "category": "부동산", "subcategory": "부동산앱", "tel": "1899-3700", "ars": "", "hours": "평일 09:00~18:00", "official": True},
    {"id": "re002", "name": "다방 고객센터", "category": "부동산", "subcategory": "부동산앱", "tel": "1588-1600", "ars": "", "hours": "평일 09:00~18:00", "official": True},
    {"id": "re003", "name": "KB부동산", "category": "부동산", "subcategory": "부동산정보", "tel": "1588-9999", "ars": "", "hours": "평일 09:00~18:00", "official": True},
    {"id": "re004", "name": "GS건설(자이)", "category": "부동산", "subcategory": "건설사", "tel": "1588-0007", "ars": "", "hours": "평일 09:00~18:00", "official": True},
    {"id": "re005", "name": "대우건설(푸르지오)", "category": "부동산", "subcategory": "건설사", "tel": "1588-0996", "ars": "", "hours": "평일 09:00~18:00", "official": True},
    {"id": "re006", "name": "현대건설(힐스테이트)", "category": "부동산", "subcategory": "건설사", "tel": "1544-5000", "ars": "", "hours": "평일 09:00~18:00", "official": True},
    {"id": "re007", "name": "롯데건설(캐슬)", "category": "부동산", "subcategory": "건설사", "tel": "1588-0100", "ars": "", "hours": "평일 09:00~18:00", "official": True},
]

# ── 보험 확장 ──
insurance_ext = [
    {"id": "ie001", "name": "메리츠화재", "category": "금융", "subcategory": "손해보험", "tel": "1566-7711", "ars": "", "hours": "24시간(사고)", "official": True},
    {"id": "ie002", "name": "한화손해보험", "category": "금융", "subcategory": "손해보험", "tel": "1566-8000", "ars": "", "hours": "24시간(사고)", "official": True},
    {"id": "ie003", "name": "흥국생명", "category": "금융", "subcategory": "생명보험", "tel": "1588-2288", "ars": "", "hours": "평일 09:00~18:00", "official": True},
    {"id": "ie004", "name": "신한생명", "category": "금융", "subcategory": "생명보험", "tel": "1544-1188", "ars": "", "hours": "평일 09:00~18:00", "official": True},
    {"id": "ie005", "name": "NH농협생명", "category": "금융", "subcategory": "생명보험", "tel": "1544-4000", "ars": "", "hours": "평일 09:00~18:00", "official": True},
    {"id": "ie006", "name": "AIA생명코리아", "category": "금융", "subcategory": "외국계보험", "tel": "1588-9898", "ars": "", "hours": "평일 09:00~18:00", "official": True},
    {"id": "ie007", "name": "메트라이프생명", "category": "금융", "subcategory": "외국계보험", "tel": "1588-9600", "ars": "", "hours": "평일 09:00~18:00", "official": True},
]

stage2 = local_gov + medical + energy + education + legal + conglomerate + foreign_ext + realestate + insurance_ext

print(f"2단계 신규 {len(stage2)}개")

# 기존 데이터 로드
with open('/Users/toctgx/golfmap-contacts/contacts_v1.json', 'r', encoding='utf-8') as f:
    v1 = json.load(f)

# 중복 제거 후 합치기
existing_ids = {c['id'] for c in v1}
new_items = [c for c in stage2 if c['id'] not in existing_ids]
all_data = v1 + new_items

from collections import Counter
cats = Counter(c['category'] for c in all_data)
print(f"\n전체 {len(all_data)}개 연락처")
for cat, count in sorted(cats.items()):
    print(f"  {cat}: {count}개")

with open('/Users/toctgx/golfmap-contacts/contacts_v1.json', 'w', encoding='utf-8') as f:
    json.dump(all_data, f, ensure_ascii=False, indent=2)

print("\n✅ contacts_v1.json 업데이트 완료")
