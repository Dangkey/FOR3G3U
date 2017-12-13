# coding=UTF-8              ATH: Nota Ã¾essa lÃ­nu ef komment eiga aÃ° vera Ã¡ Ã­slensku!!!
from yathzy import *

# Leikurinn samanstendur af 5 tenginum
dt = DiceThrower()
# og blaÃ°i(sheet) sem fyllt er Ãºt(hÃ©rna er Ã¾aÃ° frumstillt meÃ° -1)
sheet = [-1,-1,-1,-1,-1]

# Ã upphafi er spurt hvort spila skuli leik eÃ°a hÃ¦tta viÃ°.
game_is_on = main_menu()

# LeikjalÃºppan fer Ã­ gang.  HÃ©r efit spilast leikurinn algerlega innan
# hennar.
while game_is_on:
    # Ãžessi smÃ¦kkaÃ°a ÃºtgÃ¡fa af Yatzy hefur 5 hluta:
    # "litlu rÃ¶Ã°", "storu rÃ¶Ã°" "fullt hÃºs","Ã¡hÃ¦ttu" og "yatzy"
    # ÃžaÃ° Ã¾arf aÃ° kasta teningunum fyrir hvert Ã¾essara hluta.
    # Muna samt aÃ° venjulegt yatzy hefur fleiri mÃ¶guleika
    # SjÃ¡ dÃ¦mi: http://www.appgamenews.com/mobile_games/mobilegames_dice/Yatzy_HD_33_1467_1.html
    # ÃžaÃ° er vitaÃ° fyrirfram hve oft Ã¾arf aÃ° kasta svo aÃ° hÃ©r er notuÃ° for-lÃºppa.
    for i in range(0,5):
        # Kallar Ã¡ falliÃ° dice_menu() sem sÃ©r um aÃ° kasta teningunum og birta niÃ°urstÃ¶Ã°ur
        # Ã¡samt Ã¾vÃ­ aÃ° bjÃ³Ã°a spilaranum uppÃ¡ aÃ° kasta aftur(alls Ã¾risvar)
        # FalliÃ° skilar svo lokastÃ¶Ã°unni Ã¡ teningunum fimm sem sett er Ã­ breytuna dice.
        dice = dice_menu(dt)
        # sheet_menu() er svo notaÃ° til aÃ° gefa spilaranum val um hvar hann setur niÃ°urstÃ¶Ã°urnar
        sheet_menu(dice,sheet)

    # SamanlÃ¶gÃ° stig eru loksins prentur Ãºt
    print ('Final Score',sum(sheet))
    # Spilarinn er aÃ° lokum spurÃ°ur hvort hann vilji spila nÃ½jan leik eÃ°a hÃ¦tta
    game_is_on = main_menu()

print ('The End!')




