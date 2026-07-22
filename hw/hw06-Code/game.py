from hw06 import Player, TA, Boss, Weapon, Armor, Buff
import time
import random


# Define the 5 TAs
TAS = [
    {
        "name": "TA Alice", 
        "specialty": "Recursion",
        "difficulty": 1, 
        "description": "A master of recursive thinking!",
        "specialty_buff": {
            "buff": Buff("Recursive Power", attack_bonus=8, defense_bonus=0, duration=3),
            "message": "activates Recursive Power! (ATK +8)"
        }
    },
    {
        "name": "TA Bob",
        "specialty": "Data Structures",
        "difficulty": 2, 
        "description": "Expert in organizing attacks efficiently!",
        "specialty_buff": {
            "buff": Buff("Organized Defense", attack_bonus=0, defense_bonus=6, duration=3),
            "message": "organizes their defense! (DEF +6)"
        }
    },
    {
        "name": "TA Carol",
        "specialty": "Algorithms",
        "difficulty": 3, 
        "description": "Uses optimal strategies!",
        "specialty_buff": {
            "buff": Buff("Optimal Strategy", attack_bonus=5, defense_bonus=5, duration=3),
            "message": "optimizes their strategy! (ATK +5, DEF +5)"
        }
    },
    {
        "name": "TA Dave",
        "specialty": "Functional Programming",
        "difficulty": 4, 
        "description": "Composes pure attack functions!",
        "specialty_buff": {
            "buff": Buff("Pure Composition", attack_bonus=6, defense_bonus=3, duration=4),
            "message": "composes pure functions! (ATK +6, DEF +3, lasts 4 turns)"
        }
    },
    {
        "name": "TA Eve",
        "specialty": "Meta-circular Evaluation",
        "difficulty": 5, 
        "description": "Can evaluate their own power!",
        "specialty_buff": {
            "buff": Buff("Self-Evaluation", attack_bonus=7, defense_bonus=4, duration=3),
            "message": "evaluates their own power! (ATK +7, DEF +4)"
        }
    }
]


# Equipment Shop Catalog
WEAPONS_FOR_SALE = [
    Weapon("Wooden Stick", attack_bonus=3, price=30),
    Weapon("Iron Sword", attack_bonus=8, price=80),
    Weapon("Steel Blade", attack_bonus=15, price=150),
    Weapon("Mythril Saber", attack_bonus=25, price=300),
]

ARMOR_FOR_SALE = [
    Armor("Cloth Robe", defense_bonus=2, price=25),
    Armor("Leather Armor", defense_bonus=5, price=60),
    Armor("Chain Mail", defense_bonus=10, price=120),
    Armor("Plate Armor", defense_bonus=18, price=250),
]


class Battle:
    """
    Manages a turn-based battle between player and enemy.
    """
    
    def __init__(self, player, enemy):
        self._player = player
        self._enemy = enemy
        self._turn_count = 0
    
    def start(self):
        """Start the battle. Returns True if player wins, False if player loses."""
        print("\n" + "=" * 60)
        print(f"BATTLE START: {self._player.name} vs {self._enemy.name}!")
        print("=" * 60)
        print(f"\n{self._enemy.description}\n")
        
        while self._player.is_alive() and self._enemy.is_alive():
            self._turn_count += 1
            self._print_status()
            
            # Player turn
            self._player_turn()
            
            if not self._enemy.is_alive():
                break
            
            # Enemy turn
            self._enemy_turn()
        
        # Battle end
        return self._end_battle()
    
    def _print_status(self):
        """Print current battle status."""
        print(f"\n{'─' * 60}")
        print(f"Turn {self._turn_count}")
        print(f"{'─' * 60}")
        print(self._player)
        print(self._enemy)
        print()
    
    def _player_turn(self):
        """Handle player's turn."""
        while True:
            self._player.update_buffs()
            print("Your turn! Choose an action:")
            print("  1. Attack")
            print("  2. Magic Attack (causes Exhaustion: -5 ATK, -3 DEF for 2 turns)")
            print("  3. Use Potion")
            print("  4. Apply Buff")
            
            choice = input("\nEnter choice (1-4): ").strip()
            
            if choice == "1":
                message = self._player.basic_attack(self._enemy)
                print(f"\n{message}")
                return
            
            elif choice == "2":
                message = self._player.magic_attack(self._enemy)
                print(f"\n{message}")
                return
            
            elif choice == "3":
                if self._player.potions <= 0:
                    print("\n[X] You have no potions left!")
                    continue
                message = self._player.use_potion()
                print(f"\n{message}")
                return
            
            elif choice == "4":
                buff_type = input("Choose buff (1=Attack +10, 2=Defense +8): ").strip()
                if buff_type == "1":
                    buff = Buff("Attack Up", attack_bonus=8, duration=3)
                    self._player.buffs.append(buff)
                    print("\nApplied Attack Up!")
                    return
                elif buff_type == "2":
                    buff = Buff("Defense Up", defense_bonus=8, duration=3)
                    self._player.buffs.append(buff)
                    print("\nApplied Defense Up!")
                    return
            
            print("[X] Invalid choice! Try again.")
    
    def _enemy_turn(self):
        """Handle enemy's turn."""
        self._enemy.update_buffs()
        print(f"\n{self._enemy.name}'s turn!")
        message = self._enemy.choose_action(self._player)
        print(message)
    
    def _end_battle(self):
        """Handle battle end. Returns True if player won."""
        print("\n" + "=" * 60)
        
        if self._player.is_alive():
            print("VICTORY!")
            print("=" * 60)
            print(f"\nYou defeated {self._enemy.name}!")
            
            # Rewards
            self._player.gold += self._enemy.gold_reward
            print(f"Gained {self._enemy.gold_reward} gold!")
            
            level_msg = self._player.add_experience(self._enemy.exp_reward)
            print(f"Gained {self._enemy.exp_reward} experience!")
            
            if level_msg:
                print(level_msg)
            
            # Random potion drop
            if random.random() < 0.5:
                self._player.potions += 1
                print("Found a health potion!")
            
            # Small heal after battle
            heal_amount = self._player.heal(20)
            if heal_amount > 0:
                print(f"Recovered {heal_amount} HP after battle.")
            
            return True
        else:
            print("DEFEAT!")
            print("=" * 60)
            print(f"\n{self._enemy.name} has defeated you...")
            return False


class Game:
    """
    Main game controller.
    Simplified version focusing on core gameplay.
    """
    
    def __init__(self):
        self._player: Player = None
        self._current_stage = 0  # 0-4: TAs, 5: Boss
        self._game_over = False
        
        # Create the 5 TAs with their specialty buffs
        self._tas = [
            TA(ta["name"], ta["difficulty"], 
               specialty_buff=ta["specialty_buff"],
               description=ta["description"])
            for ta in TAS
        ]
        
        # Create the boss
        self._boss = Boss()
    
    def start(self):
        """Start the game."""
        self._show_intro()
        self._create_player()
        self._give_starting_equipment()
        self._main_loop()
    
    def _show_intro(self):
        """Display game introduction."""
        print("\n" + "=" * 60)
        print("SICP RPG: QUEST FOR LAMBDA")
        print("=" * 60)
        print("\nWelcome to the SICP Programming Challenge!")
        print("\nYou must defeat 5 Teaching Assistants, each specializing")
        print("in different SICP concepts. After conquering all TAs,")
        print("face the final challenge: Professor Lambda!")
        print("\nGood luck!\n")
        time.sleep(1)
    
    def _create_player(self):
        """Create player character."""
        print("=" * 60)
        name = input("Enter your character's name: ").strip()
        if not name:
            name = "Student"
        
        self._player = Player(name)
        print(f"\nWelcome, {name}!")
        print(f"Starting stats: HP={self._player.max_hp}, "
              f"ATK={self._player.get_attack()}, DEF={self._player.get_defense()}")
        print()
    
    def _give_starting_equipment(self):
        """Give player some basic equipment."""
        # Don't give equipment - let them buy it from shop
        print("You start with 50 gold. Visit the shop to buy equipment!")
        print()
    
    def _main_loop(self):
        """Main game loop."""
        while not self._game_over:
            self._show_progress()
            
            print("\nWhat would you like to do?")
            if self._current_stage < 5:
                print("  1. Challenge Next TA")
            else:
                print("  1. Challenge the Boss")
            print("  2. Visit Shop")
            print("  3. View Stats")
            print("  4. Rest (Restore HP)")
            print("  5. Quit Game")
            
            choice = input("\nEnter choice (1-5): ").strip()
            
            if choice == "1":
                self._challenge_next_enemy()
            elif choice == "2":
                self._visit_shop()
            elif choice == "3":
                self._view_stats()
            elif choice == "4":
                self._rest()
            elif choice == "5":
                self._quit_game()
            else:
                print("[X] Invalid choice!")
    
    def _show_progress(self):
        """Show game progression."""
        print("\n" + "=" * 60)
        print("MAIN MENU")
        print("=" * 60)
        print(f"Progress: {self._current_stage}/5 TAs defeated")
        print(f"Gold: {self._player.gold}")
        if self._current_stage == 5:
            print("WARNING: Ready to face the Boss!")
    
    def _challenge_next_enemy(self):
        """Challenge the next enemy."""
        if self._current_stage < 5:
            # Fight a TA
            ta = self._tas[self._current_stage]
            print(f"\nChallenging {ta.name} !")
            time.sleep(1)
            
            battle = Battle(self._player, ta)
            victory = battle.start()
            
            if victory:
                self._current_stage += 1
                
                time.sleep(2)
                
                # Check if ready for boss
                if self._current_stage == 5:
                    print("\n" + "!" * 60)
                    print("You have defeated all 5 TAs!")
                    print("Professor Lambda awaits...")
                    print("!" * 60)
                    time.sleep(2)
            else:
                # Player lost
                self._game_over = True
                print("\nGame Over! You have been defeated.")
        
        else:
            # Fight the boss
            self._challenge_boss()
    
    def _visit_shop(self):
        """Visit the equipment shop."""
        print("\n" + "=" * 60)
        print("EQUIPMENT SHOP")
        print("=" * 60)
        print(f"Your gold: {self._player.gold}")
        print("\nWelcome! What would you like to buy?")
        
        print("\n--- WEAPONS ---")
        for i, weapon in enumerate(WEAPONS_FOR_SALE, 1):
            print(f"  {i}. {weapon} - {weapon.price} gold")
        
        print("\n--- ARMOR ---")
        offset = len(WEAPONS_FOR_SALE)
        for i, armor in enumerate(ARMOR_FOR_SALE, offset + 1):
            print(f"  {i}. {armor} - {armor.price} gold")
        
        print(f"\n  {offset + len(ARMOR_FOR_SALE) + 1}. Health Potion (50 HP) - 30 gold")
        print(f"  {offset + len(ARMOR_FOR_SALE) + 2}. Leave shop")
        
        choice = input("\nEnter choice: ").strip()
        
        try:
            choice_num = int(choice)
            
            # Buying weapons
            if 1 <= choice_num <= len(WEAPONS_FOR_SALE):
                weapon = WEAPONS_FOR_SALE[choice_num - 1]
                if self._player.spend_gold(weapon.price):
                    new_weapon = Weapon(weapon.name, weapon.attack_bonus, weapon.price)
                    self._player.equip_weapon(new_weapon)
                    print(f"\n[OK] Purchased and equipped {weapon.name}!")
                else:
                    print(f"\n[X] Not enough gold! Need {weapon.price}, have {self._player.gold}")
            
            # Buying armor
            elif len(WEAPONS_FOR_SALE) < choice_num <= offset + len(ARMOR_FOR_SALE):
                armor = ARMOR_FOR_SALE[choice_num - offset - 1]
                if self._player.spend_gold(armor.price):
                    new_armor = Armor(armor.name, armor.defense_bonus, armor.price)
                    self._player.equip_armor(new_armor)
                    print(f"\n[OK] Purchased and equipped {armor.name}!")
                else:
                    print(f"\n[X] Not enough gold! Need {armor.price}, have {self._player.gold}")
            
            # Buying potion
            elif choice_num == offset + len(ARMOR_FOR_SALE) + 1:
                if self._player.spend_gold(30):
                    self._player.potions += 1
                    print("\n[OK] Purchased health potion!")
                else:
                    print(f"\n[X] Not enough gold! Need 30, have {self._player.gold}")
        
        except (ValueError, IndexError):
            pass
    
    def _give_equipment_reward(self):
        """Give player an equipment upgrade."""
        if self._current_stage == 2:
            weapon = Weapon("Iron Sword", attack_bonus=8)
            self._player.equip_weapon(weapon)
            print(f"\nYou found a {weapon}!")
        elif self._current_stage == 4:
            armor = Armor("Leather Armor", defense_bonus=5)
            self._player.equip_armor(armor)
            print(f"\nYou found {armor}!")
    
    def _challenge_boss(self):
        """Challenge the final boss."""
        print("\n" + "=" * 60)
        print("FINAL BOSS BATTLE")
        print("=" * 60)
        print("\nProfessor Lambda stands before you...")
        print("This is the ultimate test!")
        
        confirm = input("\nAre you ready? (yes/no): ").strip().lower()
        if confirm != "yes":
            print("Perhaps you need more preparation...")
            return
        
        time.sleep(1)
        
        battle = Battle(self._player, self._boss)
        victory = battle.start()
        
        if victory:
            self._show_victory_screen()
        else:
            self._game_over = True
            print("\nGame Over! The professor was too powerful.")
    
    def _show_victory_screen(self):
        """Show final victory screen."""
        print("\n" + "=" * 60)
        print("CONGRATULATIONS!")
        print("=" * 60)
        print("\nYou have defeated Professor Lambda!")
        print("You are now a Lambda Champion!")
        print(f"\nFinal Level: {self._player.level}")
        print("\nThank you for playing SICP RPG!")
        print("=" * 60)
        
        self._game_over = True
    
    def _view_stats(self):
        """View character stats."""
        print("\n" + "=" * 60)
        print("CHARACTER STATS")
        print("=" * 60)
        
        print(f"\nName: {self._player.name}")
        print(f"Level: {self._player.level}")
        print(f"Experience: {self._player.experience}/{self._player.level * 50}")
        print(f"Gold: {self._player.gold}")
        print(f"\nHP: {self._player.current_hp}/{self._player.max_hp}")
        print(f"Attack: {self._player.get_attack()}")
        print(f"Defense: {self._player.get_defense()}")
        print(f"Potions: {self._player.potions}")
    
    def _rest(self):
        """Rest to restore HP and remove exhaustion (costs 20 gold)."""
        rest_cost = 20
        
        if self._player.gold < rest_cost:
            print(f"\n[X] Not enough gold to rest! Need {rest_cost}, have {self._player.gold}")
            return
        
        # Charge gold
        self._player.spend_gold(rest_cost)
        
        # Restore HP
        healed = self._player.heal(self._player.max_hp)
        
        # Remove exhaustion buffs
        exhaustion_removed = False
        original_buffs = len(self._player.buffs)
        self._player.buffs = [b for b in self._player.buffs if b.name != "Exhaustion"]
        if len(self._player.buffs) < original_buffs:
            exhaustion_removed = True
        
        print(f"\n[Spent {rest_cost} gold]")
        if healed > 0:
            print(f"You rest and recover {healed} HP!")
        if exhaustion_removed:
            print("Exhaustion removed!")
        if healed == 0 and not exhaustion_removed:
            print("You rest but are already in perfect condition!")
    
    def _quit_game(self):
        """Quit the game."""
        confirm = input("\nAre you sure you want to quit? (yes/no): ").strip().lower()
        if confirm == "yes":
            print("\nThanks for playing! Goodbye!")
            self._game_over = True


def main():
    """Main entry point."""
    game = Game()
    game.start()


if __name__ == "__main__":
    main()
