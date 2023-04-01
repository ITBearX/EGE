f n
  | n > 2 = f (n-1) + f (n-2)
  | otherwise = n

main = print(f 17)
