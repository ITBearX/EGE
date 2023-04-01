f :: Int -> Int

f 0 = 0
f 1 = 1
f 2 = 3
f n
  | odd n = f (n-1) + f (n-3)
  | otherwise = f (n-2) + f (n `div` 2) + 1

main = print(f 35)
