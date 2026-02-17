
class Character:        #vytvoření class pro postavu
    def __init__(self,max_hp,dmg):
        self.hp = max_hp
        self.dmg = dmg
    
    def health_change(self,dmg,heal):       #změnění životů
        if self.hp == 0:        #kontrola jestli postava ještě žije
            print("game over")
        if collision with enemy_hitbox:        #odečtení poškození od životů
            self.hp = self.hp - dmg
        elif collision with heal:        #přičtení životů při léčení
            if self.hp == max_hp:
                self.hp = self.hp
            else:
                self.hp = self.hp + heal        #přičtení životů
        else:        #když se nic nestalo
            return self.hp

    def damage(self,buff,debuff):       #výpočet poškození postavy podle posílení nebo zeslabení
        if Character has buff:
            self.dmg = self.dmg * buff        
        elif Character has debuff:
            self.dmg = self.dmg * debuff
        else:        #když se nic nestalo
            return self.dmg

#už daná postava

postava = Character(20,3)
