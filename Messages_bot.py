from random import choice
from itertools import cycle
from datetime import datetime


def __main__():
    pass


def Command_doesnt_exist():
    choices = choice(['That command doesnt exist', 'That command doesnt exist you dumbfuk',
                      'WTF man,how many times do i have to tell you it doesnt exist',
                      'are you retarded?It doesnt fuking exist'])
    return choices


def Clean_error():
    choices = choice(
        ["Don't forget to specify the amount of messages to delete", 'you forgot the number of messages to delete',
         'make sure all arguments are there'])
    return choices


def random_color():
    # 209 possible colors
    colors = choice(
        [0xA17BC8, 0xC9CBE9, 0xA888B8, 0xC18EB2, 0x766359, 0x6C60A4, 0xB48BD1, 0x0DB535, 0x04B8B8, 0x022B5E, 0x8CFC69,
         0x9B027E, 0xBE6D16, 0xC8D4FE, 0x34EEFB, 0x9E261C, 0x018DD8, 0xC270ED, 0x212C9D, 0xC3DEF6, 0xA4B640, 0x1DF1E8,
         0x304C68, 0x581B79, 0x34D682, 0xB48F18, 0x93C95A, 0xE0D3F3, 0x392826, 0xE55DE1, 0xEEA32B, 0x52B1EA, 0xC5F50A,
         0xD2AA6A, 0xAFF19E, 0xAF4366, 0x629D57, 0x466CE6, 0x652A51, 0x3B32B1, 0xB808B5, 0xC94C5E, 0x600D38, 0x3227CB,
         0x43E069, 0xA0CED4, 0x77B8AA, 0x4C04AC, 0x9AD764, 0x77BD80, 0xEF9A81, 0xA7075B, 0x03294F, 0x2CEC72, 0xCBABEC,
         0x9C2007, 0x054309, 0xBF0D78, 0x6DFEE6, 0x70E9E6, 0x625B46, 0xB3F2A6, 0xCC99EB, 0xD9B123, 0xA9DD46, 0x137F0E,
         0x77EE74, 0x915C03, 0x840D80, 0xA696AB, 0xAF964A, 0xCDD082, 0xB63BF8, 0x893044, 0x548A47, 0x5625F4, 0xC96D67,
         0x90F91F, 0x0A7017, 0xDF9366, 0x1FAF91, 0xED7BE4, 0xE16B60, 0x6B466F, 0x16DC71, 0x3029EC, 0xF3D732, 0xE32CC9,
         0xFFE2EA, 0x2E088B, 0xC1BFAF, 0xB93C97, 0xEA8B78, 0x627AC3, 0xDE31A5, 0x559A8F, 0x93668A, 0xD08764, 0xF5B617,
         0x819F33, 0x0F5BFD, 0x44BC4C, 0xEE885F, 0x298B6A, 0x82B365, 0x60E3EB, 0x0D7B14, 0xF79789, 0x1BABE3, 0xC730EC,
         0x5D95FB, 0xDABCF8, 0x3A698C, 0x795D06, 0x744726, 0xB0A6BB, 0xE3CD52, 0xD76145, 0xFA8816, 0xCBC82A, 0x3DB768,
         0x026154, 0xE34B38, 0x6F5075, 0x4F69E1, 0x6AF7A9, 0x2818D5, 0x8AD4EE, 0xD27C18, 0xA86816, 0x6E9A16, 0x5FCCEB,
         0xBA507C, 0xE9F3F2, 0xBBFFFF, 0xF15CE6, 0x9A8600, 0xFAFA6F, 0x54AE5A, 0xCC3AC6, 0xE2605F, 0x3F8FFD, 0x2B878B,
         0x3C4ABD, 0xCE6118, 0xFD70D9, 0x76EDAE, 0x3AEB29, 0x77BB05, 0x6A8B87, 0xCC0157, 0x25FF57, 0x581B58, 0x5EC916,
         0x95428B, 0xD9898F, 0x337969, 0x6489DF, 0xD3C666, 0x8A2989, 0x4D02A4, 0x01031F, 0xD5E1FA, 0xE5D0AE, 0x07C0AE,
         0xC2F7D3, 0x611664, 0x0DCA45, 0x33FFBD, 0x0FF0A2, 0x1EAE19, 0x9E446E, 0xD45108, 0x823858, 0x128836, 0x11A985,
         0xB2D354, 0xF66225, 0xA3991C, 0xF1C3FF, 0xB7E54F, 0xE928DE, 0xD6DE65, 0x86D223, 0x610397, 0x1E5FAF, 0x811454,
         0x5ABA3D, 0x88831A, 0x45CB39, 0x214581, 0xD25F81, 0x50B68A, 0x5A278D, 0x1377EF, 0xA6F797, 0xA7F08F, 0xDBB574,
         0x508319, 0xD5AAA8, 0xB90E61, 0x6AB4AE, 0x2F555D, 0xF3A15D, 0xCDEC1D, 0x35D2A1, 0x188205, 0x6F468F, 0x00381B]
    )
    return colors




class timetable:
    sunday = ['Hindi/French', 'Maths', 'Economics', 'Break', 'Physics', 'Stretch', 'Biology', 'History', 'English']
    monday = ['English', 'Maths', 'Hindi/French', 'Break', 'Geography', 'Stretch', 'IT', 'NAP-eng', 'NAP-math']
    tuesday = ['Test', 'Test', 'Break', 'Maths', 'Chemistry', 'English', 'Break', 'Civics', 'NAP-science']
    wednesday = ['Hindi/French', 'English', 'Biology', 'Break', 'Maths', 'Stretch', 'Civics', 'Maths', 'IT']
    thursday = ['Geography', 'Hindi/French', 'Physics', 'Break', 'ME', 'Stretch', 'English', 'Maths', 'Chemistry']

    week = [sunday, monday, tuesday, wednesday, thursday]

    def get_day(self):
        days = int(datetime.now().weekday())
        day = timetable.week[days + 1]
        return day

    def get_time(self):
        time = int(datetime.now().strftime('%H%M'))
        return time

    def get_period(self):

        day = self.get_day()
        time = self.get_time()

        if int(datetime.now().weekday() + 1) != 2:
            if 800 <= time < 845:
                return day[0]
            elif 846 <= time < 930:
                return day[1]
            elif 931 <= time < 1015:
                return day[2]
            elif 1016 <= time < 1030:
                return day[3]
            elif 1031 <= time < 1115:
                return day[4]
            elif 1116 <= time < 1130:
                return day[5]
            elif 1131 <= time < 1215:
                return day[6]
            elif 1216 <= time < 1300:
                return day[7]
            elif 1301 <= time < 1345:
                return day[8]
            else:
                return f'No school at {datetime.now().strftime("%I:%M %p")}'

        elif int(datetime.now().weekday() + 1) == 2:
            if 755 <= time < 840:
                return day[0]
            elif 841 <= time < 935:
                return day[1]
            elif 936 <= time < 945:
                return day[2]
            elif 946 <= time < 1030:
                return day[3]
            elif 1031 <= time < 1115:
                return day[4]
            elif 1116 <= time < 1200:
                return day[5]
            elif 1131 <= time < 1215:
                return day[6]
            elif 1216 <= time < 1300:
                return day[7]
            elif 1301 <= time < 1345:
                return day[8]
            else:
                return f'No school at {datetime.now().strftime("%I:%M %p")}'

    def get_next_period(self):

        day = self.get_day()
        time = self.get_time()

        if int(datetime.now().weekday() + 1) != 2:
            if 800 <= time < 845:
                return day[1]
            elif 846 <= time < 930:
                return day[2]
            elif 931 <= time < 1015:
                return day[3]
            elif 1016 <= time < 1030:
                return day[4]
            elif 1031 <= time < 1115:
                return day[5]
            elif 1116 <= time < 1130:
                return day[6]
            elif 1131 <= time < 1215:
                return day[7]
            elif 1216 <= time < 1300:
                return day[8]
            elif 1301 <= time < 1345:
                return 'This is the last period'
            else:
                return 'School is over!'

        elif int(datetime.now().weekday() + 1) == 2:
            if 755 <= time < 840:
                return day[1]
            elif 841 <= time < 935:
                return day[2]
            elif 936 <= time < 945:
                return day[3]
            elif 946 <= time < 1030:
                return day[4]
            elif 1031 <= time < 1115:
                return day[5]
            elif 1116 <= time < 1200:
                return day[6]
            elif 1131 <= time < 1215:
                return day[7]
            elif 1216 <= time < 1300:
                return day[8]
            elif 1301 <= time < 1345:
                return 'This is the last period'
            else:
                return 'School is over!'

