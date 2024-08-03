# Chess game

## Rules

Each player submits a string consisting of `p`, `n`, `b`, `r`, `q`, `k`. Each of the characters correspond to the chess pieces pawn, knight, bishop, rook, queen, and king. Then a chess game is started, and stockfish will play the best move automatically for you. But, there is one and only constraint: **you can only move the piece corresponding to the character**. If you can't move the piece for whatever reason, you move the piece corresponding to the next piece in the string. The string is repeated over and over until the game ends.

For example, if your string is `pnbqkr`, stockfish will move a pawn on the 1st move, a knight on the 2nd move, a bishop on the 3rd move, and so on.

* Castling is considered a king move.

## Running the game

Run `main.py`

```
python main.py
```

## Example game

* white: `pnbqkr`
* black: `pnbrqk`

Move (white)|Move (black)|Move (white)|Move (black)
:-:|:-:|:-:|:-:
![](examples/board_example_1.png)|![](examples/board_example_2.png)|![](examples/board_example_3.png)|![](examples/board_example_4.png)
![](examples/board_example_5.png)|![](examples/board_example_6.png)|![](examples/board_example_7.png)|![](examples/board_example_8.png)    
![](examples/board_example_9.png)|![](examples/board_example_10.png)|![](examples/board_example_11.png)|![](examples/board_example_12.png) 
![](examples/board_example_13.png)|![](examples/board_example_14.png)|![](examples/board_example_15.png)|![](examples/board_example_16.png)
![](examples/board_example_17.png)|![](examples/board_example_18.png)|![](examples/board_example_19.png)|![](examples/board_example_20.png)
![](examples/board_example_21.png)|![](examples/board_example_22.png)|![](examples/board_example_23.png)|![](examples/board_example_24.png)
![](examples/board_example_25.png)|![](examples/board_example_26.png)|![](examples/board_example_27.png)|![](examples/board_example_28.png)
![](examples/board_example_29.png)|![](examples/board_example_30.png)|![](examples/board_example_31.png)|![](examples/board_example_32.png)
![](examples/board_example_33.png)|![](examples/board_example_34.png)|![](examples/board_example_35.png)|![](examples/board_example_36.png)
![](examples/board_example_37.png)|![](examples/board_example_38.png)|![](examples/board_example_39.png)|![](examples/board_example_40.png)
![](examples/board_example_41.png)|![](examples/board_example_42.png)|![](examples/board_example_43.png)|![](examples/board_example_44.png)
![](examples/board_example_45.png)|![](examples/board_example_46.png)|![](examples/board_example_47.png)|![](examples/board_example_48.png)
![](examples/board_example_49.png)|![](examples/board_example_50.png)|![](examples/board_example_51.png)|![](examples/board_example_52.png)
![](examples/board_example_53.png)|![](examples/board_example_54.png)|![](examples/board_example_55.png)|![](examples/board_example_56.png)
![](examples/board_example_57.png)|![](examples/board_example_58.png)|![](examples/board_example_59.png)|![](examples/board_example_60.png)
![](examples/board_example_61.png)|![](examples/board_example_62.png)|![](examples/board_example_63.png)|![](examples/board_example_64.png)
![](examples/board_example_65.png)|![](examples/board_example_66.png)|![](examples/board_example_67.png)|![](examples/board_example_68.png)
![](examples/board_example_69.png)|![](examples/board_example_70.png)|![](examples/board_example_71.png)|![](examples/board_example_72.png)
![](examples/board_example_73.png)|![](examples/board_example_74.png)|![](examples/board_example_75.png)|![](examples/board_example_76.png)
![](examples/board_example_77.png)|![](examples/board_example_78.png)|![](examples/board_example_79.png)|![](examples/board_example_80.png)
![](examples/board_example_81.png)|![](examples/board_example_82.png)|![](examples/board_example_83.png)|![](examples/board_example_84.png)
![](examples/board_example_85.png)|![](examples/board_example_86.png)|![](examples/board_example_87.png)|![](examples/board_example_88.png)
![](examples/board_example_89.png)|![](examples/board_example_90.png)|![](examples/board_example_91.png)|![](examples/board_example_92.png)
![](examples/board_example_93.png)|![](examples/board_example_94.png)|![](examples/board_example_95.png)|![](examples/board_example_96.png)
![](examples/board_example_97.png)|![](examples/board_example_98.png)|![](examples/board_example_99.png)|![](examples/board_example_100.png)
![](examples/board_example_101.png)|![](examples/board_example_102.png)|![](examples/board_example_103.png)|![](examples/board_example_104.png)
![](examples/board_example_105.png)|![](examples/board_example_106.png)|![](examples/board_example_107.png)|![](examples/board_example_108.png)
![](examples/board_example_109.png)|![](examples/board_example_110.png)|![](examples/board_example_111.png)|![](examples/board_example_112.png)
![](examples/board_example_113.png)|![](examples/board_example_114.png)|![](examples/board_example_115.png)|![](examples/board_example_116.png)
![](examples/board_example_117.png)|![](examples/board_example_118.png)|![](examples/board_example_119.png)|![](examples/board_example_120.png)
![](examples/board_example_121.png)|![](examples/board_example_122.png)|![](examples/board_example_123.png)|![](examples/board_example_124.png)
![](examples/board_example_125.png)|![](examples/board_example_126.png)|![](examples/board_example_127.png)|![](examples/board_example_128.png)
![](examples/board_example_129.png)|![](examples/board_example_130.png)|![](examples/board_example_131.png)|![](examples/board_example_132.png)
![](examples/board_example_133.png)|![](examples/board_example_134.png)|![](examples/board_example_135.png)|![](examples/board_example_136.png)
![](examples/board_example_137.png)|![](examples/board_example_138.png)|![](examples/board_example_139.png)|![](examples/board_example_140.png)
![](examples/board_example_141.png)|![](examples/board_example_142.png)|![](examples/board_example_143.png)|![](examples/board_example_144.png)
![](examples/board_example_145.png)|![](examples/board_example_146.png)|![](examples/board_example_147.png)|![](examples/board_example_148.png)
![](examples/board_example_149.png)|![](examples/board_example_150.png)|![](examples/board_example_151.png)|![](examples/board_example_152.png)
![](examples/board_example_153.png)|![](examples/board_example_154.png)|![](examples/board_example_155.png)|![](examples/board_example_156.png)
![](examples/board_example_157.png)|![](examples/board_example_158.png)|![](examples/board_example_159.png)|![](examples/board_example_160.png)