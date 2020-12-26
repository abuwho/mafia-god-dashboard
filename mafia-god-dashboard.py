from tkinter import *
from tkinter import messagebox
import random
from collections import Counter

root = Tk()
root.title('Mafia GOD Dashboard')
# root.iconbitmap('public/mafia-icon.ico')
root.geometry('1200x700')


players, roles = [], []
victims, hospitalized_people = [], []
current_players, current_roles, dead_players = [], [], []
players_n_roles = {}

# magician_is_dead = False

global roles_count
roles_count = Counter(current_roles)

global victims_count
victims_count = Counter(victims)

# Initializing the numbers as IntVar
number_of_players, number_of_mafias, number_of_villagers, number_of_doctors, number_of_sheriffs, number_of_magicians, number_of_kamikazes, number_of_maniacs = IntVar(), IntVar(), IntVar(), IntVar(), IntVar(), IntVar(), IntVar(), IntVar()
number_of_good_people, number_of_bad_people = IntVar(), IntVar()
person_mafias_kill, person_kamikaze_asks, person_magician_mutes, person_maniac_kills, person_doctor_saves, person_villagers_execute = StringVar(), StringVar(), StringVar(), StringVar(), StringVar(), StringVar()

# Define preferred font for the text areas as a tuple
preferred_text_font = ('Cambria', 10)


# function to return key for any value
def get_key(val, dictionary):
    for key, value in dictionary.items():
         if val == value:
             return key
    return "Key doesn't exist"


# Create `add_roles_to_game` function
def add_roles_to_game():
    # Firstly, clear the `roles` list
    roles.clear()

    # Then add roles to the roles array
    for m in range(number_of_mafias.get()):
        roles.append('Mafia')

    for k in range(number_of_kamikazes.get()):
        roles.append('Kamikaze')

    for d in range(number_of_doctors.get()):
        roles.append('Doctor')

    for s in range(number_of_sheriffs.get()):
        roles.append('Sheriff')

    for m in range(number_of_magicians.get()):
        roles.append('Magician')

    for m in range(number_of_maniacs.get()):
        roles.append('Maniac')

    for v in range(number_of_villagers.get()):
        roles.append('Villager')

    global current_roles
    current_roles = roles

    # Disable the entries
    number_of_players_entry.config(state=DISABLED)
    number_of_mafias_entry.config(state=DISABLED)
    number_of_villagers_entry.config(state=DISABLED)
    number_of_doctors_entry.config(state=DISABLED)
    number_of_sheriffs_entry.config(state=DISABLED)
    number_of_magicians_entry.config(state=DISABLED)
    number_of_kamikazes_entry.config(state=DISABLED)
    number_of_maniacs_entry.config(state=DISABLED)

    global number_of_effective_players
    number_of_effective_players =  number_of_mafias.get() + number_of_villagers.get() + number_of_doctors.get() +  number_of_sheriffs.get() + number_of_magicians.get() + number_of_kamikazes.get() + number_of_maniacs.get()

    if number_of_effective_players == number_of_players.get() and number_of_effective_players >= 6 and number_of_mafias.get() >= 2 and number_of_villagers.get() >= 2 and number_of_doctors.get() >= 1:
        messagebox.showinfo(title='Success!', message=f'{number_of_mafias.get()} mafias, {number_of_villagers.get()} villagers, {number_of_doctors.get()} doctor(s), {number_of_sheriffs.get()} sheriff(s), {number_of_magicians.get()} magician(s), {number_of_kamikazes.get()} kamikaze(s), and {number_of_maniacs.get()} maniac(s) have been added to the game.\n\n\nIf you would like to proceed to the next step, click `OK` and start adding the names of the players (one name in each line)\n\n\nIf you would like to change the number of players, go back to the previous screen and click the `Reset/Edit` button.')
        # Configure the `random_assignment_btn` button
        random_assignment_btn.config(text=f'Click to assign roles to these (👆) {number_of_players.get()} players randomly. (👇)', state=NORMAL)
        reshuffle_btn.config(state=NORMAL)
        # Configure the `player_names_text` text area
        player_names_text.config(state=NORMAL)
        player_names_text.delete('1.0', END)
        player_names_label.config(text=f'Name of players: \n➡➡➡➡➡➡➡\n➡➡➡➡➡➡➡\n➡➡➡➡➡➡➡\nONE PLAYER IN EACH LINE\n\nPut exactly {number_of_effective_players} names.')
    else:
        messagebox.showerror('Error!', f'Please check if your configuration (number of players and roles) is correct. \n\n1) Add at least 7 players for a fun game. \n\n2) Please make sure you add at least 2 (or more) mafias, 2 (or more) villagers, and 1 (or more) doctor. \n\nClick `Reset/Edit` to configure the number of players.')



# Create game_loop function
def random_assignment():
    # Enable the text area `assigned_roles_text`
    assigned_roles_text.config(state=NORMAL)
    # Clear the text area `assigned_roles_text`
    assigned_roles_text.delete('1.0', END)
    # Get the list of players
    global players
    players = player_names_text.get(1.0, END).split('\n')

    # Remove the extra element
    players.pop(-1)

    # Assign `current_players`
    global current_players
    current_players = players
    
    if number_of_players.get() == len(players):
        # Shuffle the players' names
        random.shuffle(players)

        # Empty the `players_n_roles` dictionary
        players_n_roles.clear()
        # Populate the `players_n_roles` dictionary
        for i in range(len(players)):
            players_n_roles[players[i]] = roles[i]
        
        # Configure the state of the `assigned_roles_text` text area to NORMAL
        assigned_roles_text.config(state=NORMAL)
        # Insert the assigned roles to the text area `assigned_roles_text`
        for i in range(len(players)):
            assigned_roles_text.insert(END, f'{players[i]} - {players_n_roles[players[i]]}\n')
        
        # Disable the text area `player_names_text`
        player_names_text.config(state=DISABLED)
        # Disable the text area `assigned_roles_text`
        assigned_roles_text.config(state=DISABLED)
        # Enable the `start_game_btn`
        start_game_btn.config(state=NORMAL)
    else:
        # Show a messagebox info
        messagebox.showerror('Error!', f'Please check if you have entered any extra line or forgot to add someone\'s name\n\nRemember: It\'s important to add the same number of players on the list. \n\nClick `Reset/Edit` to configure again.')


# Create `reset_or_edit_roles` function
def reset_or_edit_roles():
    reset_game_response = messagebox.askquestion('Are you sure? ', 'Do you really want to reset the game? ')
    if reset_game_response == 'yes':
        # Change the state of the entry widgets to NORMAL
        number_of_players_entry.config(state=NORMAL)
        number_of_mafias_entry.config(state=NORMAL)
        number_of_villagers_entry.config(state=NORMAL)
        number_of_doctors_entry.config(state=NORMAL)
        number_of_sheriffs_entry.config(state=NORMAL)
        number_of_magicians_entry.config(state=NORMAL)
        number_of_kamikazes_entry.config(state=NORMAL)
        number_of_maniacs_entry.config(state=NORMAL)

        # Enable the text area `player_names_config`
        player_names_text.config(state=NORMAL)
        # Empty the text area `player_names_config`
        player_names_text.delete('1.0', END)
        # Insert the default text into the text area `player_names_config`
        player_names_text.insert(END, f'Please configure the number of players and roles to add the names of players here.')
        # Disable the text area `player_names_config`
        player_names_text.config(state=DISABLED)
        # Disable the `random_assignment_btn` button
        random_assignment_btn.config(state=DISABLED)
        # Disable the `reshuffle_btn` button
        reshuffle_btn.config(state=DISABLED)
        # Enable the `add_roles_to_game_btn` button
        add_roles_to_game_btn.config(state=NORMAL)
        # Disable the `start_game_btn` button
        start_game_btn.config(state=DISABLED)
        # Disable the `assigned_roles_text` text area
        assigned_roles_text.config(state=DISABLED)
        # Configure the 'player_names_label' label's text
        player_names_label.config(text=f'Name of players: \n➡➡➡➡➡➡➡\n➡➡➡➡➡➡➡\n➡➡➡➡➡➡➡\nONE PLAYER IN EACH LINE')
        
        # Reconfigure the text area `assigned_roles_text`
        assigned_roles_text.config(state=NORMAL)
        assigned_roles_text.delete('1.0', END)
        assigned_roles_text.insert(END, f'The game has been reset, please configure again to start the game.')
        assigned_roles_text.config(state=DISABLED)

        # Reconfigure the text area `currently_alive_text`
        currently_alive_text.config(state=NORMAL)
        currently_alive_text.delete('1.0', END)
        currently_alive_text.insert(END, f'The game has been reset, please configure again to start the game.')
        currently_alive_text.config(state=DISABLED)

        # Reconfigure the text area `currently_dead_text`
        currently_dead_text.config(state=NORMAL)
        currently_dead_text.delete('1.0', END)
        currently_dead_text.insert(END, f'The game has been reset, please configure again to start the game.')
        currently_dead_text.config(state=DISABLED)

        # Clear the `current_players` list
        current_players.clear()
        # Clear the `dead_players` list
        dead_players.clear()
        # Clear the `current_roles` list
        current_roles.clear()

        # Disable the entries in the `game_control_frame` frame
        mafias_kill_entry.config(state=DISABLED)
        kamikaze_asks_entry.config(state=DISABLED)
        maniac_kills_entry.config(state=DISABLED)
        doctor_saves_entry.config(state=DISABLED)
        magician_mutes_entry.config(state=DISABLED)
        complete_night_btn.config(state=DISABLED)
        villagers_execute_entry.config(state=DISABLED)
        execute_person_btn.config(state=DISABLED)
        

        # Reset `number_of_good_people` and `number_of_bad_people`
        roles_count = Counter(current_roles)
        number_of_good_people.set(roles_count['Villager'] + roles_count['Doctor'] + roles_count['Sheriff'])
        number_of_bad_people.set(roles_count['Mafia'])
        
        # Disable timer related buttons and entries
        timer_duration_entry.config(state=DISABLED)
        start_timer_btn.config(state=DISABLED)
        pause_timer_btn.config(state=DISABLED)
        reset_timer_btn.config(state=DISABLED)

        # Show info on screen
        messagebox.showinfo('Success!', 'The game has been reset. You can configure the roles and number of players now. ')
    else:
        pass


# Create `start_game` function
def start_game():
    # Disable the `reshuffle_btn` button
    reshuffle_btn.config(state=DISABLED)
    # Disable the `random_assignment_btn` button
    random_assignment_btn.config(state=DISABLED)
    # Disable the `add_roles_to_game` button
    add_roles_to_game_btn.config(state=DISABLED)
    # Disable the `start_game_btn` button
    start_game_btn.config(state=DISABLED)
    # Show info on screen
    messagebox.showinfo('Success!', 'The game has started!')

    # Show number of good people and bad people
    global number_of_good_people
    global number_of_bad_people
    global roles_count
    roles_count = Counter(current_roles)
    number_of_good_people.set(roles_count['Villager'] + roles_count['Doctor'] + roles_count['Sheriff'])
    number_of_bad_people.set(roles_count['Mafia'])

    # Insert all players to `currently_alive_text` text area
    currently_alive_text.config(state=NORMAL)
    currently_alive_text.delete('1.0', END)
    global current_players
    global players_n_roles
    for player in current_players:
        currently_alive_text.insert(END, f'{player} - {players_n_roles[player]}\n')
    currently_alive_text.config(state=DISABLED)


    # Enable `complete_night_btn` buttonm
    complete_night_btn.config(state=NORMAL)

    # Enable `mafias_kill_entry` entry
    mafias_kill_entry.config(state=NORMAL)
    
    if roles_count['Kamikaze'] >= 1:
        # Enable `kamikaze_asks_entry` entry
        kamikaze_asks_entry.config(state=NORMAL)
    
    if roles_count['Maniac'] >= 1:
        # Enable `maniac_kills_entry` entry
        maniac_kills_entry.config(state=NORMAL)

    if roles_count['Doctor'] >= 1:
        # Enable `doctor_saves_entry`
        doctor_saves_entry.config(state=NORMAL)
        
    if roles_count['Magician'] >= 1:
        # Enable `magician_mutes_entry`
        magician_mutes_entry.config(state=NORMAL)
        
    # Enable timer related buttons and entries
    timer_duration_entry.config(state=NORMAL)
    start_timer_btn.config(state=NORMAL)
    # reset_timer_btn.config(state=NORMAL)



# Create `mute_player` function
def mute_player():
    global current_players
    global dead_players
    global players_n_roles
    global current_roles
    global roles_count
    the_player = person_magician_mutes.get()
    mute_response = messagebox.askquestion('Are you sure? ', f'Are you sure you want to mute {the_player}?')

    if mute_response == 'yes':
        if the_player in current_players:
            # Show info via messagebox
            messagebox.showinfo('Muted!', f'{the_player} was muted. ')
            # Update the `currently_alive_text` text area
            currently_alive_text.config(state=NORMAL)
            currently_alive_text.delete('1.0', END)
            for p in current_players:
                if p == the_player:
                    currently_alive_text.insert(END, f'{p} - {players_n_roles[p]} - (MUTED)\n')
                else: 
                    currently_alive_text.insert(END, f'{p} - {players_n_roles[p]}\n')
            currently_alive_text.config(state=DISABLED)

        else:
            messagebox.showwarning('Warning!', f'{the_player} was not found on the list of alive players. Please enter the correct name. ')
    else:
        messagebox.showinfo('Game Info', f'Okay, {the_player} won\'t be muted. ')

    # Clear the `mute_player_entry` entry
    magician_mutes_entry.delete(0, 'end')

# Create `night_activities` function
def night_activities():
    confirmation = messagebox.askquestion('Confirmation', 'Are you sure you want to proceed? \n\nPlease check if all the names are correct.')
    if confirmation == 'yes':
        global victims_count
        global victims
        global hospitalized_people
        global current_players
        global dead_players
        global players_n_roles
        global roles_count
        # global magician_is_dead
        

        # Populate the `victims` list
        if len(person_mafias_kill.get()) > 0:
            victims.append(person_mafias_kill.get())
        if len(person_kamikaze_asks.get()) > 0 and players_n_roles[person_kamikaze_asks.get()] == 'Sheriff':
            victims.append(person_kamikaze_asks.get())
        if len(person_maniac_kills.get()) > 0:
            victims.append(person_maniac_kills.get())

        # Populate the `hospitalized_people` list
        if len(person_doctor_saves.get()) > 0:
            hospitalized_people.append(person_doctor_saves.get())

        if person_doctor_saves.get() in victims:
            # Remove the person who survived from the `victims` list
            victims.remove(person_doctor_saves.get())
            
        
        # Kill the rest of the victims
        for the_player in victims:
            kill_response = messagebox.askquestion('Are you sure? ', f'Are you sure you want to kill {the_player}?')
            if kill_response == 'yes':
                if the_player in current_players:
                    # if (players_n_roles[the_player] == 'Magician'):
                    #     magician_is_dead = True
                    if (players_n_roles[the_player] == 'Sheriff' and 'Kamikaze' in current_roles):
                        # Kill the Kamikaze too
                        current_roles.remove('Kamikaze')
                        kamikaze = get_key('Kamikaze', players_n_roles)
                        dead_players.append(kamikaze)
                        current_players.remove(kamikaze)
                        
                        # Add the player to the list `dead_players`
                        dead_players.append(the_player)
                        # Remove the player from the list `current_players`
                        current_players.remove(the_player)
                        # Show info via messagebox
                        messagebox.showinfo('Killed!', f'{the_player} was killed. ')
                        
                        
                        # Update the `currently_alive_text` text area
                        currently_alive_text.config(state=NORMAL)
                        currently_alive_text.delete('1.0', END)
                        for p in current_players:
                            currently_alive_text.insert(END, f'{p} - {players_n_roles[p]}\n')
                        currently_alive_text.config(state=DISABLED)
                        # Update the `currently_dead_text` text area
                        currently_dead_text.config(state=NORMAL)
                        currently_dead_text.delete('1.0', END)
                        for p in dead_players:
                            currently_dead_text.insert(END, f'{p} - {players_n_roles[p]}\n')
                        currently_dead_text.config(state=DISABLED)

                        # Update the `currently_alive_text` text area
                        currently_alive_text.config(state=NORMAL)
                        currently_alive_text.delete('1.0', END)
                        for p in current_players:
                            currently_alive_text.insert(END, f'{p} - {players_n_roles[p]}\n')
                        currently_alive_text.config(state=DISABLED)
                        # Update the `currently_dead_text` text area
                        currently_dead_text.config(state=NORMAL)
                        currently_dead_text.delete('1.0', END)
                        for p in dead_players:
                            currently_dead_text.insert(END, f'{p} - {players_n_roles[p]}\n')
                        currently_dead_text.config(state=DISABLED)
                        # Remove the role `current_roles` list
                        current_roles.remove(players_n_roles[the_player])
                        # Update number of good people and bad people
                        global roles_count
                        roles_count = Counter(current_roles)
                        number_of_good_people.set(roles_count['Villager'] + roles_count['Doctor'] + roles_count['Sheriff'])
                        number_of_bad_people.set(roles_count['Mafia'])
                        
                    else:
                        # Add the player to the list `dead_players`
                        dead_players.append(the_player)
                        # Remove the player from the list `current_players`
                        current_players.remove(the_player)
                        # Show info via messagebox
                        messagebox.showinfo('Killed!', f'{the_player} was killed. ')
                        
                        # Update the `currently_alive_text` text area
                        currently_alive_text.config(state=NORMAL)
                        currently_alive_text.delete('1.0', END)
                        for p in current_players:
                            currently_alive_text.insert(END, f'{p} - {players_n_roles[p]}\n')
                        currently_alive_text.config(state=DISABLED)
                        # Update the `currently_dead_text` text area
                        currently_dead_text.config(state=NORMAL)
                        currently_dead_text.delete('1.0', END)
                        for p in dead_players:
                            currently_dead_text.insert(END, f'{p} - {players_n_roles[p]}\n')
                        currently_dead_text.config(state=DISABLED)

                        # Update the `currently_alive_text` text area
                        currently_alive_text.config(state=NORMAL)
                        currently_alive_text.delete('1.0', END)
                        for p in current_players:
                            currently_alive_text.insert(END, f'{p} - {players_n_roles[p]}\n')
                        currently_alive_text.config(state=DISABLED)
                        # Update the `currently_dead_text` text area
                        currently_dead_text.config(state=NORMAL)
                        currently_dead_text.delete('1.0', END)
                        for p in dead_players:
                            currently_dead_text.insert(END, f'{p} - {players_n_roles[p]}\n')
                        currently_dead_text.config(state=DISABLED)
                        # Remove the role `current_roles` list
                        current_roles.remove(players_n_roles[the_player])
                        # Update number of good people and bad people
                        # global roles_count
                        roles_count = Counter(current_roles)
                        number_of_good_people.set(roles_count['Villager'] + roles_count['Doctor'] + roles_count['Sheriff'])
                        number_of_bad_people.set(roles_count['Mafia'])
                        
                else:
                    messagebox.showwarning('Warning!', f'{the_player} was not found on the list of alive players. Please enter the correct name. ')
            else:
                messagebox.showinfo('Game Info', f'Okay, {the_player} won\'t be killed. ')


        # Mute Player
        # magician = get_key('Magician', players_n_roles)
        # if 'Magician' in current_roles or magician_is_dead == False:
        mute_player()
            # magician_is_dead = False


        # Empty the entries and then disable them
        mafias_kill_entry.delete(0, 'end')
        mafias_kill_entry.config(state=DISABLED)
        kamikaze_asks_entry.delete(0, 'end')
        kamikaze_asks_entry.config(state=DISABLED)
        maniac_kills_entry.delete(0, 'end')
        maniac_kills_entry.config(state=DISABLED)
        doctor_saves_entry.delete(0, 'end')
        doctor_saves_entry.config(state=DISABLED)
        magician_mutes_entry.delete(0, 'end')
        magician_mutes_entry.config(state=DISABLED)

        # Enable `villagers_execute_entry` entry
        villagers_execute_entry.config(state=NORMAL)
        # Enable `execute_person_btn` button
        execute_person_btn.config(state=NORMAL)
        # Disable the `complete_night_btn` button
        complete_night_btn.config(state=DISABLED)

        # Clear the `victims` and `hospitalized_people` lists
        victims.clear()
        hospitalized_people.clear()

    else:
        pass


# Create `execute_player` function
def execute_player():
    global current_players
    global dead_players
    global players_n_roles
    global current_roles
    global roles_count
    # global magician_is_dead
    
    the_player = person_villagers_execute.get()
    execute_response = messagebox.askquestion('Are you sure? ', f'Are you sure you want to execute {the_player}?')

    if execute_response == 'yes':
        if the_player in current_players:
            
            # if (players_n_roles[the_player] == 'Magician'):
            #     magician_is_dead = False

            # Add the player to the list `dead_players`
            dead_players.append(the_player)
            # Remove the player from the list `current_players`
            current_players.remove(the_player)
            # Show info via messagebox
            messagebox.showinfo('Executed!', f'{the_player} was executed. ')
            if (players_n_roles[the_player] == 'Sheriff' and 'Kamikaze' in roles):
                kamikaze = get_key('Kamikaze', players_n_roles)
                kill_kami_response = messagebox.askquestion(f'Execute {kamikaze} too (The Kamikaze)? ', 'Do you want to execute the {kamikaze} along with the Sheriff? ')
                if kill_kami_response == 'yes':
                    # Kill the kamikaze too
                    current_roles.remove('Kamikaze')
                    dead_players.append(kamikaze)
                    current_players.remove(kamikaze)
                    # Update the `currently_alive_text` text area
                    currently_alive_text.config(state=NORMAL)
                    currently_alive_text.delete('1.0', END)
                    for p in current_players:
                        currently_alive_text.insert(END, f'{p} - {players_n_roles[p]}\n')
                    currently_alive_text.config(state=DISABLED)
                    # Update the `currently_dead_text` text area
                    currently_dead_text.config(state=NORMAL)
                    currently_dead_text.delete('1.0', END)
                    for p in dead_players:
                        currently_dead_text.insert(END, f'{p} - {players_n_roles[p]}\n')
                    currently_dead_text.config(state=DISABLED)
                else:
                    # Kill him in next round no matter what
                    pass

            # Update the `currently_alive_text` text area
            currently_alive_text.config(state=NORMAL)
            currently_alive_text.delete('1.0', END)
            for p in current_players:
                currently_alive_text.insert(END, f'{p} - {players_n_roles[p]}\n')
            currently_alive_text.config(state=DISABLED)
            # Update the `currently_dead_text` text area
            currently_dead_text.config(state=NORMAL)
            currently_dead_text.delete('1.0', END)
            for p in dead_players:
                currently_dead_text.insert(END, f'{p} - {players_n_roles[p]}\n')
            currently_dead_text.config(state=DISABLED)
            # Remove the role `current_roles` list
            current_roles.remove(players_n_roles[the_player])
            # Update number of good people and bad people
            global roles_count
            roles_count = Counter(current_roles)
            number_of_good_people.set(roles_count['Villager'] + roles_count['Doctor'] + roles_count['Sheriff'])
            number_of_bad_people.set(roles_count['Mafia'])

        else:
            messagebox.showwarning('Warning!', 'The player was not found on the list of alive players. Please enter the correct name. ')
    else:
        pass
        messagebox.showinfo('Game Info', f'Okay, {the_player} won\'t be executed. ')


    villagers_execute_entry.delete(0, 'end')

    # Enable the `complete_night_btn` button
    complete_night_btn.config(state=NORMAL)

    if roles_count['Mafia'] >= 1:
        # Enable `mafias_kill_entry` entry
        mafias_kill_entry.config(state=NORMAL)
    
    if roles_count['Kamikaze'] >= 1:
        # Enable `kamikaze_asks_entry` entry
        kamikaze_asks_entry.config(state=NORMAL)
    
    if roles_count['Maniac'] >= 1:
        # Enable `maniac_kills_entry` entry
        maniac_kills_entry.config(state=NORMAL)

    if roles_count['Doctor'] >= 1:
        # Enable `doctor_saves_entry`
        doctor_saves_entry.config(state=NORMAL)
    
    magician_mutes_entry.config(state=NORMAL)
        
        
    # Disable `execute_person_btn` button and `villagers_execute_entry` entry
    execute_person_btn.config(state=DISABLED)
    villagers_execute_entry.config(state=DISABLED)


timer_is_paused = False
# Create `start_timer` function
def start_timer():
    global timer_is_paused
    if int(timer_duration.get()) > 0:            
        # Ask question
        timer_response = messagebox.askquestion('Confirmation', 'Do you want to start the timer now? ')
        if timer_response == 'yes':
            timer_is_paused = False
            # Disable the `timer_duration_entry` entry
            timer_duration_entry.config(state=DISABLED)
            # Disable the `start_timer_btn` button
            start_timer_btn.config(state=DISABLED)
            # Enable the `pause_timer_btn` button
            pause_timer_btn.config(state=NORMAL)

            duration = timer_duration.get()*60
            global current
            current = duration
            mins, secs = divmod(duration, 60) 
            timer = '{:02d}:{:02d}'.format(mins, secs)
            timer_display_label.config(text=timer)
            
            # Enable the `reset_timer_btn` button
            reset_timer_btn.config(state=NORMAL)
            update_timer()
            
        else:
            pass
    else:
        messagebox.showerror('Error!', 'You gave a wrong input as the duration of the timer. Please put a valid number (greater than zero).')


# Create `update_timer` function
def update_timer():
    global current
    global timer_is_paused
    if timer_is_paused == False:
        mins, secs = divmod(current, 60)
        current -= 1
        timer = '{:02d}:{:02d}'.format(mins, secs)
        timer_display_label.config(text=timer)
        if current >= 0:
            timer_display_label.after(1000, update_timer)
        else:
            messagebox.showinfo('Time\'s up!', 'The timer has been reset.')
            # Disable the `pause_timer_btn` button
            pause_timer_btn.config(state=DISABLED)
            # Enable the `start_timer_btn` button
            start_timer_btn.config(state=NORMAL)
            # Enable the `timer_duration_entry` entry
            timer_duration_entry.config(state=NORMAL)
            # Disable `reset_timer_btn` button
            reset_timer_btn.config(state=DISABLED)

# Create `pause_timer` function
def pause_timer():
    global timer_is_paused
    timer_is_paused = not timer_is_paused
    if timer_is_paused == True:
        pause_timer_btn.config(text='Resume Timer')
        timer_display_label.config(fg='red', bg='white')
    else:
        pause_timer_btn.config(text='Pause Timer')
        timer_display_label.config(fg='green', bg='black')
    update_timer()
    

# Create `reset_timer` function
def reset_timer():
    global timer_is_paused
    global reset_timer_response
    reset_timer_response = messagebox.askquestion('Confirm', 'Do you want to reset the timer? ')
    if reset_timer_response == 'yes':
        global current
        current = 0
        timer_display_label.config(text='00:00', fg='green', bg='black')
        
        messagebox.showinfo('Success!', 'The timer has been reset.')
        

        # Enable `timer_duration_entry` entry
        timer_duration_entry.config(state=NORMAL)
        # Enable `start_timer_btn` button
        start_timer_btn.config(state=NORMAL)
        # Disable the `pause_timer_btn` button
        pause_timer_btn.config(state=DISABLED)
        # Disable the `reset_timer_btn` button
        timer_is_paused = False
    else:
        pass


# Create `game_setup_frame` frame
game_setup_frame = Frame(root, bg='#61fffa', highlightbackground="#999999", highlightthickness=1)
game_setup_frame.grid(row=0, column=0, pady=20, padx=5)

# For number of players
number_of_players_label = Label(game_setup_frame, text='Number of players: ', font=preferred_text_font)
number_of_players_label.grid(row=0, column=0)
number_of_players_entry = Entry(game_setup_frame, textvariable=number_of_players, font=preferred_text_font)
number_of_players_entry.grid(row=0, column=1)

# For number of mafias
number_of_mafias_label = Label(game_setup_frame, text='Number of mafias: ', font=preferred_text_font)
number_of_mafias_label.grid(row=1, column=0)
number_of_mafias_entry = Entry(game_setup_frame, textvariable=number_of_mafias, font=preferred_text_font)
number_of_mafias_entry.grid(row=1, column=1)

# For number of villagers
number_of_villagers_label = Label(game_setup_frame, text='Number of villagers: ', font=preferred_text_font)
number_of_villagers_label.grid(row=2, column=0)
number_of_villagers_entry = Entry(game_setup_frame, textvariable=number_of_villagers, font=preferred_text_font)
number_of_villagers_entry.grid(row=2, column=1)

# For number of doctors
number_of_doctors_label = Label(game_setup_frame, text='Number of doctor(s): ', font=preferred_text_font)
number_of_doctors_label.grid(row=3, column=0)
number_of_doctors_entry = Entry(game_setup_frame, textvariable=number_of_doctors, font=preferred_text_font)
number_of_doctors_entry.grid(row=3, column=1)

# For number of sheriffs
number_of_sheriffs_label = Label(game_setup_frame, text='Number of sheriff(s): ', font=preferred_text_font)
number_of_sheriffs_label.grid(row=4, column=0)
number_of_sheriffs_entry = Entry(game_setup_frame, textvariable=number_of_sheriffs, font=preferred_text_font)
number_of_sheriffs_entry.grid(row=4, column=1)

# For number of magicians
number_of_magicians_label = Label(game_setup_frame, text='Number of magician(s): ', font=preferred_text_font)
number_of_magicians_label.grid(row=5, column=0)
number_of_magicians_entry = Entry(game_setup_frame, textvariable=number_of_magicians, font=preferred_text_font)
number_of_magicians_entry.grid(row=5, column=1)

# For number of kamikazes
number_of_kamikazes_label = Label(game_setup_frame, text='Number of kamikaze(s): ', font=preferred_text_font)
number_of_kamikazes_label.grid(row=6, column=0)
number_of_kamikazes_entry = Entry(game_setup_frame, textvariable=number_of_kamikazes, font=preferred_text_font)
number_of_kamikazes_entry.grid(row=6, column=1)

# For number of maniacs
number_of_maniacs_label = Label(game_setup_frame, text='Number of maniac(s): ', font=preferred_text_font)
number_of_maniacs_label.grid(row=7, column=0)
number_of_maniacs_entry = Entry(game_setup_frame, textvariable=number_of_maniacs, font=preferred_text_font)
number_of_maniacs_entry.grid(row=7, column=1)

# Add roles to game button
add_roles_to_game_btn = Button(game_setup_frame, text='Add these Roles to the Game', command=add_roles_to_game, font=preferred_text_font, fg='green', relief=RAISED)
add_roles_to_game_btn.grid(row=8, column=1, pady=10, padx=20)
reset_or_edit_roles_btn = Button(game_setup_frame, text='Reset/Edit', command=reset_or_edit_roles, font=preferred_text_font, fg='orange', relief=RAISED)
reset_or_edit_roles_btn.grid(row=8, column=2, pady=10, sticky='E')

# For player names
player_names_label = Label(game_setup_frame, text=f'Name of players: \n➡➡➡➡➡➡➡\n➡➡➡➡➡➡➡\n➡➡➡➡➡➡➡\nONE PLAYER IN EACH LINE', font=preferred_text_font)
player_names_label.grid(row=9, column=0)
player_names_text = Text(game_setup_frame, height=12, width=25, font=preferred_text_font)
player_names_text.grid(row=9, column=1, pady=10)
player_names_text.insert(END, f'Please configure the number of players and roles to add the names of players here.')
player_names_text.config(state=DISABLED)

# Random assign button
random_assignment_btn = Button(game_setup_frame, text=f'Assign Roles Randomly', state=DISABLED, command=random_assignment, font=preferred_text_font, fg='green', relief=RAISED)
random_assignment_btn.grid(row=10, column=0, columnspan=2, pady=10)
# Create button for reshuffling the roles
reshuffle_btn = Button(game_setup_frame, text='Reshuffle', state=DISABLED, command=random_assignment, font=preferred_text_font, fg='green', relief=RAISED)
reshuffle_btn.grid(row=10, column=2, pady=10)


# For showing assigned roles
assigned_roles_label = Label(game_setup_frame, text='The assigned roles are: \n➡➡➡➡➡➡➡\n➡➡➡➡➡➡➡\n➡➡➡➡➡➡➡\nYou can reshuffle if you want', font=preferred_text_font)
assigned_roles_label.grid(row=11, column=0)
assigned_roles_text = Text(game_setup_frame, height=12, width=25, font=preferred_text_font, state=DISABLED)
assigned_roles_text.grid(row=11, column=1, pady=10)
start_game_btn = Button(game_setup_frame, text='Start Game', state=DISABLED, command=start_game, font=preferred_text_font, fg='green', relief=RAISED)
start_game_btn.grid(row=11, column=2, pady=10)


# Create `game_status_frame` frame
game_status_frame = Frame(root, bg='#61fffa', highlightbackground="#999999", highlightthickness=1)
game_status_frame.grid(row=0, column=1, pady=20, padx=5)

# Create `timer_frame` frame
timer_frame = Frame(game_status_frame, bg='#61fffa')
timer_frame.grid(row=0, column=0, columnspan=2, pady=20)

# Create `timer_label` label
timer_display_label = Label(timer_frame, text='00:00', font=('Helvetica', 48), fg='green', bg='black')
timer_display_label.grid(row=0, column=0, columnspan=3, pady=10)

timer_duration = IntVar()
# Create `timer_duration_entry` entry
timer_duration_entry = Entry(timer_frame, textvariable=timer_duration, state=DISABLED)
timer_duration_entry.grid(row=1, column=0, pady=10)

# Create `timer_duration_label` label
timer_duration_label = Label(timer_frame, text='minutes', font=preferred_text_font)
timer_duration_label.grid(row=1, column=1, pady=10)

# Create `start_timer_btn` button
start_timer_btn = Button(timer_frame, text='Start Timer', command=start_timer, relief=RAISED, font=preferred_text_font, state=DISABLED)
start_timer_btn.grid(row=2, column=0, pady=10)

# Create `pause_timer_btn` button
pause_timer_btn = Button(timer_frame, text='Pause Timer', command=pause_timer, relief=RAISED, font=preferred_text_font, state=DISABLED)
pause_timer_btn.grid(row=2, column=1, pady=10, padx=10)

# Create `reset_timer_btn` button
reset_timer_btn = Button(timer_frame, text='Reset Timer', command=reset_timer, relief=RAISED, font=preferred_text_font, state=DISABLED)
reset_timer_btn.grid(row=2, column=2, pady=10, padx=10)




# Label for showing number of good people
good_people_label = Label(game_status_frame, text='Number of good people: ', font=preferred_text_font)
good_people_label.grid(row=1, column=0)

# Label for number of bad people
bad_people_label = Label(game_status_frame, text='Number of bad people: ', font=preferred_text_font)
bad_people_label.grid(row=2, column=0)

# Label showing the number of good people
number_of_good_people_label = Label(game_status_frame, textvariable=number_of_good_people, font=preferred_text_font)
number_of_good_people_label.grid(row=1, column=1, pady=10)
# Label showing the number of bad people
number_of_bad_people_label = Label(game_status_frame, textvariable=number_of_bad_people, font=preferred_text_font)
number_of_bad_people_label.grid(row=2, column=1, pady=10)

# Label for currently alive players
currently_alive_label = Label(game_status_frame, text='Currently Alive Players: ', font=preferred_text_font, fg='green')
currently_alive_label.grid(row=3, column=0, pady=10)
# Text area for currently alive players
currently_alive_text = Text(game_status_frame, height=12, width=25, font=preferred_text_font, state=DISABLED)
currently_alive_text.grid(row=3, column=1, pady=10)

# Label for currently dead players
currently_dead_label = Label(game_status_frame, text='Dead Players: \n\n\n\nThey may rest in peace', font=preferred_text_font)
currently_dead_label.grid(row=4, column=0, pady=10, padx=10)
# Text area for currently dead players
currently_dead_text = Text(game_status_frame, height=8, width=25, font=preferred_text_font, state=DISABLED)
currently_dead_text.grid(row=4, column=1, pady=10, padx=10)



# Create `game_control_frame` frame
game_control_frame = Frame(root, bg='#61fffa', highlightbackground="#999999", highlightthickness=1)
game_control_frame.grid(row=0, column=2, padx=5, pady=20)


# Create `mafias_kill_label` label
mafias_kill_label = Label(game_control_frame, text='Mafias kill (👉)', font=preferred_text_font, fg='red')
mafias_kill_label.grid(row=0, column=0, pady=10)

# Create `mafias_kill_entry` entry
mafias_kill_entry = Entry(game_control_frame, fg='red', font=preferred_text_font, state=DISABLED, textvariable=person_mafias_kill)
mafias_kill_entry.grid(row=0, column=1, padx=20, pady=10)

# Create `kamikaze_asks_label` label
kamikaze_asks_label = Label(game_control_frame, text='Kamikaze asks (👉)', font=preferred_text_font, fg='red')
kamikaze_asks_label.grid(row=1, column=0, pady=10)

# Create `kamikaze_asks_entry` entry
kamikaze_asks_entry = Entry(game_control_frame, fg='red', font=preferred_text_font, state=DISABLED, textvariable=person_kamikaze_asks)
kamikaze_asks_entry.grid(row=1, column=1, padx=20, pady=10)

# Create `maniac_kills_label` label
maniac_kills_label = Label(game_control_frame, text='Maniac kills (👉)', font=preferred_text_font, fg='red')
maniac_kills_label.grid(row=2, column=0, pady=10)

# Create `maniac_kills_entry` entry
maniac_kills_entry = Entry(game_control_frame, fg='red', font=preferred_text_font, state=DISABLED, textvariable=person_maniac_kills)
maniac_kills_entry.grid(row=2, column=1, padx=20, pady=10)

# Create `doctor_saves_label` label
doctor_saves_label = Label(game_control_frame, text='Doctor saves (👉) ', font=preferred_text_font, fg='green')
doctor_saves_label.grid(row=3, column=0, pady=10)

# Create `doctor_saves_entry` entry
doctor_saves_entry = Entry(game_control_frame, fg='green', font=preferred_text_font, state=DISABLED, textvariable=person_doctor_saves)
doctor_saves_entry.grid(row=3, column=1, padx=20, pady=10)

# Create `magician_mutes_label` label
magician_mutes_label = Label(game_control_frame, text='Magician mutes (👉) ', font=preferred_text_font)
magician_mutes_label.grid(row=4, column=0, pady=10)

# Create `magician_mutes_entry` entry
magician_mutes_entry = Entry(game_control_frame, font=preferred_text_font, state=DISABLED, textvariable=person_magician_mutes)
magician_mutes_entry.grid(row=4, column=1, padx=20, pady=10)


# Create `complete_night_btn` button
complete_night_btn = Button(game_control_frame, text='Complete the Night', font=preferred_text_font, state=DISABLED, command=night_activities)
complete_night_btn.grid(row=5, column=0, columnspan=2, padx=20, pady=20)


# Create `villagers_execute_label` label
villagers_execute_label = Label(game_control_frame, text='Villagers execute (👉) ', font=preferred_text_font, fg='red')
villagers_execute_label.grid(row=6, column=0, padx=20)

# Create `villagers_execute_entry` entry
villagers_execute_entry = Entry(game_control_frame, fg='red', font=preferred_text_font, state=DISABLED, textvariable=person_villagers_execute)
villagers_execute_entry.grid(row=6, column=1, pady=10, padx=20)

# Create `execute_person_btn` button
execute_person_btn = Button(game_control_frame, text='Execute This Person (👆) ', font=preferred_text_font, state=DISABLED, command=execute_player)
execute_person_btn.grid(row=7, column=0, columnspan=2, pady=20, padx=10)


# Run the mainloop function
root.mainloop()