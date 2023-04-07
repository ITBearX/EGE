import System.IO
import Data.List

main = do
  line <- readFile "data/24-01.txt"
  print $ maximum (map length (group line))
