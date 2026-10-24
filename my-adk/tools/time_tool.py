from datetime import datetime
def get_current_time() -> str:
 """
 현재 시간을 반환합니다.
 """

 now = datetime.now()
 
 return now.strftime("%Y-%m-%d %H:%M:%S")