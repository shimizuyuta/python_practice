# 前期売り上げ
first_h_sales = [
  300_000_000, 220_000_000, 340_000_000, 
  420_000_000, 410_000_000, 290_000_000
]
# 後期売り上げ
second_h_sales = [
    230_000_000, 120_000_000, 440_000_000, 
    100_000_000, 280_000_000, 390_000_000
]

# total_sales = first_h_sales.extend(second_h_sales)
# extendは破壊的なメソッドのため、この場合返り値がnoneになりエラーが生じる
total_sales = first_h_sales + second_h_sales

print('==== 2021年売り上げ ====')
print(f'前期: {sum(first_h_sales):,}円')
print(f'後期: {sum(second_h_sales):,}円')
print(f'合計: {sum(total_sales):,}円')
print('====================')