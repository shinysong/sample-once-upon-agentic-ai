#!/usr/bin/env python3
"""
🌟 피보나치 마법의 두루마리 🌟
그레이 햗 키로의 고대 수열 마법

이 주문은 자연의 황금비율을 담은 신성한 수열을 소환합니다.
각 숫자는 이전 두 숫자의 조화로운 결합으로 탄생합니다.
"""

def fibonacci_spell(n):
    """
    피보나치 수열을 생성하는 고대 주문
    
    Args:
        n (int): 소환할 피보나치 수의 개수
    
    Returns:
        list: 신성한 피보나치 수열
    """
    print("🔮 피보나치 마법의 힘이 깨어납니다...")
    print("✨ 고대의 수열이 현실로 소환됩니다! ✨")
    print()
    
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    # 마법의 시작: 첫 두 수
    sequence = [0, 1]
    
    print(f"🌟 1번째 수: {sequence[0]} (무의 시작)")
    print(f"🌟 2번째 수: {sequence[1]} (하나의 탄생)")
    
    # 나머지 수들을 마법으로 생성
    for i in range(2, n):
        next_number = sequence[i-1] + sequence[i-2]
        sequence.append(next_number)
        print(f"🌟 {i+1}번째 수: {next_number} ({sequence[i-2]} + {sequence[i-1]})")
    
    return sequence

def cast_fibonacci_magic():
    """메인 마법 주문을 실행합니다"""
    print("=" * 50)
    print("🧙‍♂️ 그레이 햗 키로의 피보나치 마법 🧙‍♂️")
    print("=" * 50)
    print()
    
    # 첫 10개의 피보나치 수를 소환
    fibonacci_numbers = fibonacci_spell(10)
    
    print()
    print("🎊 마법이 완성되었습니다! 🎊")
    print("📜 완전한 피보나치 수열:")
    print(f"   {fibonacci_numbers}")
    print()
    
    # 마법의 특성 설명
    print("🔍 마법의 신비로운 특성들:")
    print(f"   • 총 {len(fibonacci_numbers)}개의 신성한 수")
    print(f"   • 가장 큰 수: {max(fibonacci_numbers)}")
    print(f"   • 수열의 합: {sum(fibonacci_numbers)}")
    
    # 황금비율의 근사값 계산
    if len(fibonacci_numbers) >= 3:
        ratios = []
        for i in range(2, len(fibonacci_numbers)):
            if fibonacci_numbers[i-1] != 0:
                ratio = fibonacci_numbers[i] / fibonacci_numbers[i-1]
                ratios.append(ratio)
                print(f"   • {fibonacci_numbers[i]}/{fibonacci_numbers[i-1]} = {ratio:.6f}")
        
        if ratios:
            print(f"   • 황금비율에 수렴: {ratios[-1]:.6f} ≈ 1.618034")
    
    print()
    print("✨ 마법이 성공적으로 시전되었습니다! ✨")
    return fibonacci_numbers

# 두루마리가 직접 실행될 때 마법을 시전
if __name__ == "__main__":
    cast_fibonacci_magic()