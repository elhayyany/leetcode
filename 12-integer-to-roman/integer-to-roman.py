class Solution:
    def intToRoman(self, num: int) -> str:
        ones = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']
        tens = ["","X","XX","XXX","XL","L","LX","LXX","LXXX","XC"]
        hans = ["","C","CC","CCC","CD","D","DC","DCC","DCCC","CM"]
        tous = ["","M","MM","MMM"]
        return (tous[num//1000] + hans[(num % 1000) // 100] + tens[num%100 // 10] + ones[(num % 10)])


        