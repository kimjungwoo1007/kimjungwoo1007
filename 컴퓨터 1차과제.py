def calculate_veigar_ap(champ_hits, champ_kills, minion_kills, monster_kills):
    # 패시브로 얻는 주문력
    passive_ap_from_champ_hits = champ_hits * 1
    passive_ap_from_champ_kills = champ_kills * 1

    # Q 스킬로 얻는 주문력
    q_ap_from_kills = (minion_kills + monster_kills + champ_kills) * 1

    # 총 주문력 계산
    total_ap = passive_ap_from_champ_hits + passive_ap_from_champ_kills + q_ap_from_kills

    return total_ap


def main():
    print("베이가 주문력 계산기")

    while True:
        user_input = input("게임 시간을 입력하세요 (종료하려면 'q'를 입력하세요): ")

        if user_input.lower() == 'q':
            print("프로그램을 종료합니다.")
            break

        try:
            game_time = int(user_input)

            if game_time < 0:
                print("게임 시간은 0 이상이어야 합니다.")
                continue

            champ_hits = int(input("챔피언 타격 횟수: "))
            champ_kills = int(input("챔피언 처치 횟수: "))
            minion_kills = int(input("미니언 처치 횟수: "))
            monster_kills = int(input("몬스터 처치 횟수: "))

            if champ_hits < 0 or champ_kills < 0 or minion_kills < 0 or monster_kills < 0:
                print("입력 값은 0 이상이어야 합니다.")
                continue

            # 주문력 계산
            total_ap = calculate_veigar_ap(champ_hits, champ_kills, minion_kills, monster_kills)
            print(f"게임 시간 {game_time}분 동안 베이가가 획득한 총 주문력: {total_ap}")

        except ValueError:
            print("유효한 숫자를 입력하세요.")


if __name__ == "__main__":
    main()
