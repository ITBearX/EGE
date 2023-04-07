import System.IO
import Data.Char

solve :: String -> Integer
solve line = maximum $ filter (<10^9) nums where
  nums = map (\s -> read s :: Integer) (words line')
  line' = [if isDigit c then c else ' ' | c <- line]

main = do
  line <- readFile "data/24-16.txt"
  print $ solve line
