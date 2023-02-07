# -*- coding: utf-8 -*-
# cd C:\Users\alecc\AppData\Local\Programs\Python\Python39
# get-pip.py
# python get-pip.py
# python -m ensurepip --upgrade
# cd C:\Users\alecc\AppData\Local\Programs\Python\Python39\Scripts
# pip install keyboard
# pour mp3
# pip install pygame --pre


# pip install pydub
# git clone https://git.ffmpeg.org/ffmpeg.git ffmpeg
# curl -O https://ffmpeg.org/releases/ffmpeg-snapshot.tar.bz2

# pip install ffmpeg --use-pep517


# pour trouver localisation de ffmpeg
# pip show ffmpeg
# installation du programe sudo apt-get install ffmpeg

###################

# sond infinit
# sound = pygame.mixer.Sound("audio.ogg")
# sound.play(-1)



################################
# Improte
try:
    import pygame
    print("Pygame est installé et importé correctement.")
except ImportError:
    print("Pygame n'est pas installé ou n'a pas été importé correctement.")
try:
    import keyboard
    print("keyboard est installé et importé correctement.")
except ImportError:
    print("keyboard n'est pas installé ou n'a pas été importé correctement.")
try:
    import os
    print("os est installé et importé correctement.")
except ImportError:
    print("os n'est pas installé ou n'a pas été importé correctement.")
################################

from pydub import AudioSegment
import simpleaudio as sa
# os.environ["FFMPEG_BINARY"] = "C:\Users\\alecc\AppData\Local\Programs\Python\Python311\Lib\site-packages\\ffmpeg"








# from pydub import AudioSegment
# import ffmpeg

# Définir ffmpeg comme le convertisseur audio pour pydub
# AudioSegment.converter = "ffmpeg"




Rassine = "/home/add/KeyGitar/son"

# Basse
Basse_001 = Rassine + "/Basse/102_C_SizzleBass_699.mp3"
Basse_002 = Rassine + "/Basse/118_B_PhattySubBass_01_550.mp3"
Basse_003 = Rassine + "/Basse/120_Bb_PoppersBass_SP_78_01.mp3"
Basse_004 = Rassine + "/Basse/120_D_Brass_01_235_SP.mp3"
Basse_005 = Rassine + "/Basse/130_Cm_Industrial_SP_219_01.mp3"
Basse_006 = Rassine + "/Basse/135_F#m_Bassline_SP_310_02.mp3"
Basse_007 = Rassine + "/Basse/90_Gm_EightBass_01_334_SP.mp3"
Basse_008 = Rassine + "/Basse/C_ReeceBass_01_96_SP.mp3"
Basse_009 = Rassine + "/Basse/C_SubDropBass_03_632.mp3"
Basse_010 = Rassine + "/Basse/E_ArtfclIntllgnc_01_178_SP.mp3"
Basse_011 = Rassine + "/Basse/E_Bass_12_151_SP.mp3"
Basse_012 = Rassine + "/Basse/F#_BassRise_01_166_SP.mp3"
Basse_013 = Rassine + "/Basse/F_Bass_295_SP_06.mp3"
Basse_014 = Rassine + "/Basse/F_Donk_345_02.mp3"
Basse_015 = Rassine + "/Basse/Modulated_Bass_01_B2_SP_414_SP.mp3"


# Chorale
Chorale_001 = Rassine + "/Chorale/130_F_Choir_01_82_SP.mp3"
Chorale_002 = Rassine + "/Chorale/145_Cm_Choir_01_82_SP.mp3"
Chorale_003 = Rassine + "/Chorale/65_C_Choir_01_82_SP.mp3"
Chorale_004 = Rassine + "/Chorale/75_Fm_Choir_01_82_SP.mp3"

# Drum
Drum_001 = Rassine + "/Drum/100_DrumSolo_SP_236_1.mp3"
Drum_002 = Rassine + "/Drum/110_DiscoDrums_058_172_SP.mp3"
Drum_003 = Rassine + "/Drum/110_Dm_Cream_Drums_226_SP.mp3"
Drum_004 = Rassine + "/Drum/117_ZeroDrumloop_01_169_SP.mp3"
Drum_005 = Rassine + "/Drum/120_DrmsElctrTps_01_156_SP.mp3"
Drum_006 = Rassine + "/Drum/127_Loop_18_243_SP.mp3"
Drum_007 = Rassine + "/Drum/180_5-4_TghtGhst_02_173_SP.mp3"
Drum_008 = Rassine + "/Drum/85_AnalogueDrums_06_21_SP.mp3"
Drum_009 = Rassine + "/Drum/90_CrnchyBrksDry_47_64_SP.mp3"
Drum_010 = Rassine + "/Drum/95_AnalogueDrums_40_21_SP.mp3"

# Drum_Hit
Drum_Hit_001 = Rassine + "/Drum_Hit/Boom_SP_01.mp3"
Drum_Hit_002 = Rassine + "/Drum_Hit/Clash_SP_01.mp3"
Drum_Hit_003 = Rassine + "/Drum_Hit/Clicktom_SP_01.mp3"
Drum_Hit_004 = Rassine + "/Drum_Hit/Punch_SP_01.mp3"
Drum_Hit_005 = Rassine + "/Drum_Hit/Splash_SP_01.mp3"
Drum_Hit_006 = Rassine + "/Drum_Hit/Swell_SP_01.mp3"

# Embiance
Embiance_001 = Rassine + "/Embiance/105_ShaftAmbience_01_622.mp3"
Embiance_002 = Rassine + "/Embiance/127_E_SoilentGreen_243_SP.mp3"
Embiance_003 = Rassine + "/Embiance/35_G#_Skyfire_01_100_SP.mp3"
Embiance_004 = Rassine + "/Embiance/60_Am_WidePadTexture_852.mp3"
Embiance_005 = Rassine + "/Embiance/60_C#_StringsTexture_02_852.mp3"
Embiance_006 = Rassine + "/Embiance/60_C_ScratchyPadTexture_852.mp3"
Embiance_007 = Rassine + "/Embiance/70_G#_FountainAtmos_02_852.mp3"
Embiance_008 = Rassine + "/Embiance/70_G_StepDownAtmos_852.mp3"
Embiance_009 = Rassine + "/Embiance/77_E_RidgeAmbience_01_622.mp3"
Embiance_010 = Rassine + "/Embiance/85_Bb_RichAmbience_01_678.mp3"
Embiance_011 = Rassine + "/Embiance/90_C_SataAmbience_01_622.mp3"
Embiance_012 = Rassine + "/Embiance/Dm_ContemplateAmbience_06_678.mp3"
Embiance_013 = Rassine + "/Embiance/Eb_Atmos_10_170_SP.mp3"
Embiance_014 = Rassine + "/Embiance/Eb_UnassumingAtmos_718.mp3"
Embiance_015 = Rassine + "/Embiance/E_PercussiveAtmos_718.mp3"

# Numerique
Numerique_001 = Rassine + "/Numerique/ResoDistPerc_01_231_SP.mp3"

# Piano_Electrique
Piano_Electrique_001 = Rassine + "/Piano_Electrique/100_C#_AikoKeys_01_61_SP.mp3"
Piano_Electrique_002 = Rassine + "/Piano_Electrique/120_B_ChrdsRhds_02_235_SP.mp3"
Piano_Electrique_003 = Rassine + "/Piano_Electrique/120_B_ChrdsRhds_03_235_SP.mp3"
Piano_Electrique_004 = Rassine + "/Piano_Electrique/120_D_ChrdsRhds_02_235_SP.mp3"
Piano_Electrique_005 = Rassine + "/Piano_Electrique/120_D_GoodendPiano_01_659.mp3"
Piano_Electrique_006 = Rassine + "/Piano_Electrique/130_Cm_Chord_03_224_SP.mp3"
Piano_Electrique_007 = Rassine + "/Piano_Electrique/70_G_Music_SP_62_04.mp3"
Piano_Electrique_008 = Rassine + "/Piano_Electrique/95_Am_LushElectricPiano_08_583.mp3"
Piano_Electrique_009 = Rassine + "/Piano_Electrique/Dm_FlowChrdEPiano_02_687.mp3"

# Record
Record_001 = Rassine + "/Record/Found1_331_47.mp3"

# Ritme
Ritme_001 = Rassine + "/Ritme/110_B_Brass_10_SP.mp3"
Ritme_002 = Rassine + "/Ritme/115_D#_Climbing_01_100_SP.mp3"
Ritme_003 = Rassine + "/Ritme/122_C#m_MidnightLead_23_671.mp3"
Ritme_004 = Rassine + "/Ritme/125_Emin_13_Lead4_99_SP.mp3"
Ritme_005 = Rassine + "/Ritme/128_D#_Pluck_SP_238_12.mp3"
Ritme_006 = Rassine + "/Ritme/128_F#m_Chords_SP_230_01.mp3"
Ritme_007 = Rassine + "/Ritme/165_F#_ArpLoop_01_173_SP.mp3"
Ritme_008 = Rassine + "/Ritme/74_A_04_OhYeah388_SP.mp3"
Ritme_009 = Rassine + "/Ritme/86_F#m_PhasaahVocal_01_577.mp3"
Ritme_010 = Rassine + "/Ritme/89_Abm_YayVocal_01_612.mp3"
Ritme_011 = Rassine + "/Ritme/BritneysDead_127_G_101_SP03.mp3"
Ritme_012 = Rassine + "/Ritme/Chase_127_E_101_SP01.mp3"
Ritme_013 = Rassine + "/Ritme/Chase_127_E_101_SP04.mp3"
Ritme_014 = Rassine + "/Ritme/Cheese_127_C_101_SP02.mp3"
Ritme_015 = Rassine + "/Ritme/DeathOrg_127_E_101_SP01.mp3"
Ritme_016 = Rassine + "/Ritme/Dense_127_F_101_SP03.mp3"
Ritme_017 = Rassine + "/Ritme/Dense_127_F_101_SP04.mp3"
Ritme_018 = Rassine + "/Ritme/Epic_127_E_101_SP01.mp3"
Ritme_019 = Rassine + "/Ritme/Glisten_127_E_101_SP02.mp3"
Ritme_020 = Rassine + "/Ritme/Hit_127_F_101_SP02.mp3"
Ritme_021 = Rassine + "/Ritme/Hit_127_F_101_SP04.mp3"
Ritme_022 = Rassine + "/Ritme/Hit_127_F_101_SP06.mp3"
Ritme_023 = Rassine + "/Ritme/Interlude_127_B_101_SP02.mp3"
Ritme_024 = Rassine + "/Ritme/Knocking_127_B_101_SP01.mp3"
Ritme_025 = Rassine + "/Ritme/Light_127_G_101_SP03.mp3"
Ritme_026 = Rassine + "/Ritme/looperman-l-1319133-0318341-acid-tb-303-roland.wav"
Ritme_027 = Rassine + "/Ritme/looperman-l-1351931-0098694-kadoonthetrack-trap-melody-1.wav"
Ritme_028 = Rassine + "/Ritme/looperman-l-1724442-0206916-chill-electric-guitar.wav"
Ritme_029 = Rassine + "/Ritme/looperman-l-2109380-0113815-alex4747-deep-house-synth-and-bass.wav"
Ritme_030 = Rassine + "/Ritme/looperman-l-2572734-0320040-rodeo-emotional-synth-loop.wav"
Ritme_031 = Rassine + "/Ritme/looperman-l-2921269-0155797-wah-guitar-riff-2.wav"
Ritme_032 = Rassine + "/Ritme/looperman-l-2926297-0174860-sad-guitar-loop-soulless-by-jkeibeats.wav"
Ritme_033 = Rassine + "/Ritme/looperman-l-3047107-0162847-never.wav"
Ritme_034 = Rassine + "/Ritme/looperman-l-3121345-0227095-melodic-vibes.wav"
Ritme_035 = Rassine + "/Ritme/looperman-l-3181879-0218428-guitar-fight.wav"
Ritme_036 = Rassine + "/Ritme/looperman-l-4652704-0317597-synth-arp-space.wav"
Ritme_037 = Rassine + "/Ritme/looperman-l-4684541-0318413-16-difourks-punch-bass-130bpm-c.wav"
Ritme_038 = Rassine + "/Ritme/looperman-l-5220523-0322101-humor-rjpasin.wav"
Ritme_039 = Rassine + "/Ritme/Mega_130_D_101_SP01.mp3"
Ritme_040 = Rassine + "/Ritme/Miami_127_B_101_SP02.mp3"
Ritme_041 = Rassine + "/Ritme/Modular_127_E_101_SP04.mp3"
Ritme_042 = Rassine + "/Ritme/OldSynth_127_B_101_SP06.mp3"
Ritme_043 = Rassine + "/Ritme/Phasey_127_E_101_SP03.mp3"
Ritme_044 = Rassine + "/Ritme/Pop_130_G_101_SP03.mp3"
Ritme_045 = Rassine + "/Ritme/Positive_127_G_101_SP01.mp3"
Ritme_046 = Rassine + "/Ritme/Positive_127_G_101_SP02.mp3"
Ritme_047 = Rassine + "/Ritme/Positive_127_G_101_SP03.mp3"
Ritme_048 = Rassine + "/Ritme/Psyche_127_E_101_SP02.mp3"
Ritme_049 = Rassine + "/Ritme/Pumping_127_G_101_SP01.mp3"
Ritme_050 = Rassine + "/Ritme/Raw_127_D_101_SP04.mp3"
Ritme_051 = Rassine + "/Ritme/Rush_127_B_101_SP02.mp3"
Ritme_052 = Rassine + "/Ritme/Sawtable_127_Bf_101_SP03.mp3"
Ritme_053 = Rassine + "/Ritme/Sensitive_127_E_101_SP02.mp3"
Ritme_054 = Rassine + "/Ritme/Shadows_120_Af_101_SP02.mp3"
Ritme_055 = Rassine + "/Ritme/Softly_127_B_101_SP01.mp3"
Ritme_056 = Rassine + "/Ritme/Spacy_120_A_101_SP01.mp3"
Ritme_057 = Rassine + "/Ritme/Synthy_120_A_101_SP03.mp3"
Ritme_058 = Rassine + "/Ritme/Techy_127_G_101_SP01.mp3"
Ritme_059 = Rassine + "/Ritme/Unison_127_Bf_101_SP01.mp3"
Ritme_060 = Rassine + "/Ritme/Unison_127_Bf_101_SP02.mp3"
Ritme_061 = Rassine + "/Ritme/WarmFuzz_120_C_101_SP02.mp3"
Ritme_062 = Rassine + "/Ritme/WarmFuzz_120_C_101_SP03.mp3"





audio = AudioSegment.from_file(Ritme_008)
temp_file = "Ritme_008"
sound.export(temp_file, format="mp3")

wave_obj = sa.WaveObject.from_wave_file(temp_file)
play_obj = wave_obj.play()






pygame.init()



def ricord():
    text = ""
    while True:
        event = pygame.event.wait()
        if event.type == pygame.KEYDOWN:
            if event.unicode.isalnum() or event.unicode.isspace():
                text += event.unicode
            if event.key == pygame.K_SPACE:
                break
            if event.key == pygame.K_RETURN:
                text += "\n"
        return text



def play_sound_q():
    print("Q")
    print(Ritme_008)
    pygame.mixer.music.load(Ritme_008)
    pygame.mixer.music.play()

def play_sound_w():
    print("W")
    pygame.mixer.music.load(Ritme_002)
    pygame.mixer.music.play()

def play_sound_e():
    pygame.mixer.music.load(Ritme_003)
    pygame.mixer.music.play()

def play_sound_r():
    pygame.mixer.music.load(Ritme_004)
    pygame.mixer.music.play()

def play_sound_t():
    pygame.mixer.music.load(Ritme_005)
    pygame.mixer.music.play()

def play_sound_z():
    pygame.mixer.music.load(Ritme_006)
    pygame.mixer.music.play()

def play_sound_u():
    pygame.mixer.music.load(Ritme_007)
    pygame.mixer.music.play()

def play_sound_i():
    pygame.mixer.music.load(Ritme_008)
    pygame.mixer.music.play()

def play_sound_o():
    pygame.mixer.music.load(Ritme_009)
    pygame.mixer.music.play()

def play_sound_p():
    pygame.mixer.music.load(Ritme_010)
    pygame.mixer.music.play()

def play_sound_a():
    pygame.mixer.music.load(Piano_Electrique_007)
    pygame.mixer.music.play()

def play_sound_s():
    pygame.mixer.music.load(Piano_Electrique_008)
    pygame.mixer.music.play()

def play_sound_d():
    pygame.mixer.music.load(Piano_Electrique_009)
    pygame.mixer.music.play()

def play_sound_f():
    pygame.mixer.music.load(Piano_Electrique_006)
    pygame.mixer.music.play()

def play_sound_g():
    pygame.mixer.music.load(Embiance_001)
    pygame.mixer.music.play()

def play_sound_h():
    pygame.mixer.music.load(Embiance_002)
    pygame.mixer.music.play()

def play_sound_j():
    pygame.mixer.music.load(Embiance_003)
    pygame.mixer.music.play()

def play_sound_k():
    pygame.mixer.music.load(Embiance_004)
    pygame.mixer.music.play()

def play_sound_l():
    pygame.mixer.music.load(Embiance_005)
    pygame.mixer.music.play()

def play_sound_y():
    pygame.mixer.music.load(Embiance_006)
    pygame.mixer.music.play()

def play_sound_x():
    pygame.mixer.music.load(Embiance_007)
    pygame.mixer.music.play()

def play_sound_c():
    pygame.mixer.music.load(Embiance_008)
    pygame.mixer.music.play()

def play_sound_v():
    pygame.mixer.music.load(Embiance_009)
    pygame.mixer.music.play()

def play_sound_b():
    pygame.mixer.music.load(Embiance_010)
    pygame.mixer.music.play()

def play_sound_n():
    pygame.mixer.music.load(Embiance_011)
    pygame.mixer.music.play()

def play_sound_m():
    pygame.mixer.music.load(Embiance_012)
    pygame.mixer.music.play()







keyboard.add_hotkey("q", play_sound_q)
keyboard.add_hotkey("w", play_sound_w)
keyboard.add_hotkey("e", play_sound_e)
keyboard.add_hotkey("r", play_sound_r)
keyboard.add_hotkey("t", play_sound_t)
keyboard.add_hotkey("z", play_sound_z)
keyboard.add_hotkey("u", play_sound_u)
keyboard.add_hotkey("i", play_sound_i)
keyboard.add_hotkey("o", play_sound_o)
keyboard.add_hotkey("p", play_sound_p)
keyboard.add_hotkey("a", play_sound_a)
keyboard.add_hotkey("s", play_sound_s)
keyboard.add_hotkey("d", play_sound_d)
keyboard.add_hotkey("f", play_sound_f)
keyboard.add_hotkey("g", play_sound_g)
keyboard.add_hotkey("h", play_sound_h)
keyboard.add_hotkey("j", play_sound_j)
keyboard.add_hotkey("k", play_sound_k)
keyboard.add_hotkey("l", play_sound_l)
keyboard.add_hotkey("y", play_sound_y)
keyboard.add_hotkey("x", play_sound_x)
keyboard.add_hotkey("c", play_sound_c)
keyboard.add_hotkey("v", play_sound_v)
keyboard.add_hotkey("b", play_sound_b)
keyboard.add_hotkey("n", play_sound_n)
keyboard.add_hotkey("m", play_sound_m)




keyboard.add_hotkey("-", lambda: keyboard.remove_hotkey("f5"))

while True:
    keyboard.wait()


