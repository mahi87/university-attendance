from attendance import Attendance

if __name__ == "__main__":
    try:
        days = int(input("Number of Academic days: "))
    except Exception as e:
        raise ValueError(f'Invalid input provided: {e}')
    
    else:
        at = Attendance(days)
        print(f"Probability to miss Grad Ceremony: {at.probability_to_miss_grad_ceremony()}")