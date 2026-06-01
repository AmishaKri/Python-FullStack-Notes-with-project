def infiniteChai():
    cnt=1
    while True:
        yield f"refill {cnt}"
        cnt+=1
        
refill=infiniteChai()
    
for _ in range(5):
    print(next(refill))