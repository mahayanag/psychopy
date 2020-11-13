#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.2.5),
    on Fri Nov 13 15:12:50 2020
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2020.2.5'
expName = 'atitude'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sort_keys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/mahayanagodoy/Documents/Mahayana/academics/cursos/PUCRS/Psychopy/Aulas/Aula3/experimento_atitude/atitude_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.DEBUG)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1280, 800], fullscr=False, screen=0, 
    winType='pyglet', allowGUI=True, allowStencil=False,
    monitor='testMonitor', color=[0.929,0.969,0.969], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "instrucoes"
instrucoesClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='default text',
    font='Arial',
    pos=(0, 0.2), height=0.04, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
passagem_instrucoes = visual.TextStim(win=win, name='passagem_instrucoes',
    text='Aperte ESPAÇO para continuar',
    font='Arial',
    pos=(0, -0.3), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
passagemBarra_instrucoes = keyboard.Keyboard()

# Initialize components for Routine "aviso_caracteristica"
aviso_caracteristicaClock = core.Clock()
aviso_txt = visual.TextStim(win=win, name='aviso_txt',
    text='default text',
    font='Arial',
    pos=(0, 0.2), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
text_2 = visual.TextStim(win=win, name='text_2',
    text='Aperte ESPAÇO para ouvir o áudio',
    font='Arial',
    pos=(0, -0.2), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
passagem_aviso = keyboard.Keyboard()

# Initialize components for Routine "experimento"
experimentoClock = core.Clock()
ouca = visual.TextStim(win=win, name='ouca',
    text='Ouça o áudio',
    font='Arial',
    pos=(0, 0.4), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
sound_clip = sound.Sound('A', secs=-1, stereo=True, hamming=True,
    name='sound_clip')
sound_clip.setVolume(1)
repetir = visual.TextStim(win=win, name='repetir',
    text='Aperte “r” se desejar ouvir o áudio novamente',
    font='Arial',
    pos=(0, 0.3), height=0.03, wrapWidth=None, ori=0, 
    color='red', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
slider = visual.Slider(win=win, name='slider',
    size=(1.0, 0.1), pos=(0, -0.2), units='height',
    labels=("1 = pouco", "2", "3", "4", "5 = muito"), ticks=(1, 2, 3, 4, 5),
    granularity=1, style=['rating', 'triangleMarker'],
    color='black', font='HelveticaBold',
    flip=False, depth=-5)
passagem = visual.TextStim(win=win, name='passagem',
    text='Aperte ESPAÇO para continuar',
    font='Arial',
    pos=(0, -0.4), height=0.03, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);
passagemBarra = keyboard.Keyboard()
pergunta = visual.TextStim(win=win, name='pergunta',
    text='default text',
    font='Arial',
    pos=(0, 0.1), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-8.0);
ISI = clock.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI')

# Initialize components for Routine "final"
finalClock = core.Clock()
text_3 = visual.TextStim(win=win, name='text_3',
    text='O experimento acabou!\n\nMuito obrigado!',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# set up handler to look after randomisation of conditions etc
instructions = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('instrucoes.xlsx'),
    seed=None, name='instructions')
thisExp.addLoop(instructions)  # add the loop to the experiment
thisInstruction = instructions.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisInstruction.rgb)
if thisInstruction != None:
    for paramName in thisInstruction:
        exec('{} = thisInstruction[paramName]'.format(paramName))

for thisInstruction in instructions:
    currentLoop = instructions
    # abbreviate parameter names if possible (e.g. rgb = thisInstruction.rgb)
    if thisInstruction != None:
        for paramName in thisInstruction:
            exec('{} = thisInstruction[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "instrucoes"-------
    continueRoutine = True
    # update component parameters for each repeat
    text.setText(instrucoestxt)
    passagemBarra_instrucoes.keys = []
    passagemBarra_instrucoes.rt = []
    _passagemBarra_instrucoes_allKeys = []
    # keep track of which components have finished
    instrucoesComponents = [text, passagem_instrucoes, passagemBarra_instrucoes]
    for thisComponent in instrucoesComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    instrucoesClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "instrucoes"-------
    while continueRoutine:
        # get current time
        t = instrucoesClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=instrucoesClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text* updates
        if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text.frameNStart = frameN  # exact frame index
            text.tStart = t  # local t and not account for scr refresh
            text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
            text.setAutoDraw(True)
        
        # *passagem_instrucoes* updates
        if passagem_instrucoes.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            passagem_instrucoes.frameNStart = frameN  # exact frame index
            passagem_instrucoes.tStart = t  # local t and not account for scr refresh
            passagem_instrucoes.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(passagem_instrucoes, 'tStartRefresh')  # time at next scr refresh
            passagem_instrucoes.setAutoDraw(True)
        
        # *passagemBarra_instrucoes* updates
        waitOnFlip = False
        if passagemBarra_instrucoes.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            passagemBarra_instrucoes.frameNStart = frameN  # exact frame index
            passagemBarra_instrucoes.tStart = t  # local t and not account for scr refresh
            passagemBarra_instrucoes.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(passagemBarra_instrucoes, 'tStartRefresh')  # time at next scr refresh
            passagemBarra_instrucoes.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(passagemBarra_instrucoes.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(passagemBarra_instrucoes.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if passagemBarra_instrucoes.status == STARTED and not waitOnFlip:
            theseKeys = passagemBarra_instrucoes.getKeys(keyList=['space'], waitRelease=False)
            _passagemBarra_instrucoes_allKeys.extend(theseKeys)
            if len(_passagemBarra_instrucoes_allKeys):
                passagemBarra_instrucoes.keys = _passagemBarra_instrucoes_allKeys[-1].name  # just the last key pressed
                passagemBarra_instrucoes.rt = _passagemBarra_instrucoes_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instrucoesComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "instrucoes"-------
    for thisComponent in instrucoesComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    instructions.addData('text.started', text.tStartRefresh)
    instructions.addData('text.stopped', text.tStopRefresh)
    instructions.addData('passagem_instrucoes.started', passagem_instrucoes.tStartRefresh)
    instructions.addData('passagem_instrucoes.stopped', passagem_instrucoes.tStopRefresh)
    # the Routine "instrucoes" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'instructions'


# set up handler to look after randomisation of conditions etc
loop_experimento = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('experimentais.xlsx'),
    seed=None, name='loop_experimento')
thisExp.addLoop(loop_experimento)  # add the loop to the experiment
thisLoop_experimento = loop_experimento.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisLoop_experimento.rgb)
if thisLoop_experimento != None:
    for paramName in thisLoop_experimento:
        exec('{} = thisLoop_experimento[paramName]'.format(paramName))

for thisLoop_experimento in loop_experimento:
    currentLoop = loop_experimento
    # abbreviate parameter names if possible (e.g. rgb = thisLoop_experimento.rgb)
    if thisLoop_experimento != None:
        for paramName in thisLoop_experimento:
            exec('{} = thisLoop_experimento[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "aviso_caracteristica"-------
    continueRoutine = True
    # update component parameters for each repeat
    aviso_txt.setText(aviso)
    passagem_aviso.keys = []
    passagem_aviso.rt = []
    _passagem_aviso_allKeys = []
    # keep track of which components have finished
    aviso_caracteristicaComponents = [aviso_txt, text_2, passagem_aviso]
    for thisComponent in aviso_caracteristicaComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    aviso_caracteristicaClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "aviso_caracteristica"-------
    while continueRoutine:
        # get current time
        t = aviso_caracteristicaClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=aviso_caracteristicaClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *aviso_txt* updates
        if aviso_txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            aviso_txt.frameNStart = frameN  # exact frame index
            aviso_txt.tStart = t  # local t and not account for scr refresh
            aviso_txt.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(aviso_txt, 'tStartRefresh')  # time at next scr refresh
            aviso_txt.setAutoDraw(True)
        
        # *text_2* updates
        if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_2.frameNStart = frameN  # exact frame index
            text_2.tStart = t  # local t and not account for scr refresh
            text_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
            text_2.setAutoDraw(True)
        
        # *passagem_aviso* updates
        waitOnFlip = False
        if passagem_aviso.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            passagem_aviso.frameNStart = frameN  # exact frame index
            passagem_aviso.tStart = t  # local t and not account for scr refresh
            passagem_aviso.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(passagem_aviso, 'tStartRefresh')  # time at next scr refresh
            passagem_aviso.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(passagem_aviso.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(passagem_aviso.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if passagem_aviso.status == STARTED and not waitOnFlip:
            theseKeys = passagem_aviso.getKeys(keyList=['space'], waitRelease=False)
            _passagem_aviso_allKeys.extend(theseKeys)
            if len(_passagem_aviso_allKeys):
                passagem_aviso.keys = _passagem_aviso_allKeys[-1].name  # just the last key pressed
                passagem_aviso.rt = _passagem_aviso_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in aviso_caracteristicaComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "aviso_caracteristica"-------
    for thisComponent in aviso_caracteristicaComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    loop_experimento.addData('aviso_txt.started', aviso_txt.tStartRefresh)
    loop_experimento.addData('aviso_txt.stopped', aviso_txt.tStopRefresh)
    loop_experimento.addData('text_2.started', text_2.tStartRefresh)
    loop_experimento.addData('text_2.stopped', text_2.tStopRefresh)
    # the Routine "aviso_caracteristica" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "experimento"-------
    continueRoutine = True
    # update component parameters for each repeat
    sound_clip.setSound(som, hamming=True)
    sound_clip.setVolume(1, log=False)
    def playSound():
        beep = sound.Sound(som, secs=.3)  # You will probably need to add your sound variable e.g. 'Sound'
        beep.setVolume(1)
        beep.play()
        core.wait(.3)
    slider = visual.Slider(win=win, name='slider',
        size=(0.5, 0.1), pos=(0, -0.1),
        labels=['1 \npouco', '3', '5 \nmuito'], ticks=(1, 2, 3, 4, 5),
        granularity=1, style=('triangleMarker'),
        color='black', font='HelveticaBold',
        flip=False, labelHeight = .03)
    slider.marker.size=(.05,.05)
    slider.reset()
    passagemBarra.keys = []
    passagemBarra.rt = []
    _passagemBarra_allKeys = []
    pergunta.setText(clique)
    # keep track of which components have finished
    experimentoComponents = [ouca, sound_clip, repetir, slider, passagem, passagemBarra, pergunta, ISI]
    for thisComponent in experimentoComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    experimentoClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "experimento"-------
    while continueRoutine:
        # get current time
        t = experimentoClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=experimentoClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *ouca* updates
        if ouca.status == NOT_STARTED and tThisFlip >= 3-frameTolerance:
            # keep track of start time/frame for later
            ouca.frameNStart = frameN  # exact frame index
            ouca.tStart = t  # local t and not account for scr refresh
            ouca.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ouca, 'tStartRefresh')  # time at next scr refresh
            ouca.setAutoDraw(True)
        # start/stop sound_clip
        if sound_clip.status == NOT_STARTED and tThisFlip >= 3-frameTolerance:
            # keep track of start time/frame for later
            sound_clip.frameNStart = frameN  # exact frame index
            sound_clip.tStart = t  # local t and not account for scr refresh
            sound_clip.tStartRefresh = tThisFlipGlobal  # on global time
            sound_clip.play(when=win)  # sync with win flip
        
        # *repetir* updates
        if repetir.status == NOT_STARTED and sound_clip.status==FINISHED:
            # keep track of start time/frame for later
            repetir.frameNStart = frameN  # exact frame index
            repetir.tStart = t  # local t and not account for scr refresh
            repetir.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(repetir, 'tStartRefresh')  # time at next scr refresh
            repetir.setAutoDraw(True)
        if event.getKeys(keyList=["r"]):
            playSound()
        
        # *slider* updates
        if slider.status == NOT_STARTED and sound_clip.status==FINISHED:
            # keep track of start time/frame for later
            slider.frameNStart = frameN  # exact frame index
            slider.tStart = t  # local t and not account for scr refresh
            slider.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(slider, 'tStartRefresh')  # time at next scr refresh
            slider.setAutoDraw(True)
        
        # *passagem* updates
        if passagem.status == NOT_STARTED and sound_clip.status==FINISHED:
            # keep track of start time/frame for later
            passagem.frameNStart = frameN  # exact frame index
            passagem.tStart = t  # local t and not account for scr refresh
            passagem.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(passagem, 'tStartRefresh')  # time at next scr refresh
            passagem.setAutoDraw(True)
        
        # *passagemBarra* updates
        waitOnFlip = False
        if passagemBarra.status == NOT_STARTED and sound_clip.status==FINISHED:
            # keep track of start time/frame for later
            passagemBarra.frameNStart = frameN  # exact frame index
            passagemBarra.tStart = t  # local t and not account for scr refresh
            passagemBarra.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(passagemBarra, 'tStartRefresh')  # time at next scr refresh
            passagemBarra.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(passagemBarra.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(passagemBarra.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if passagemBarra.status == STARTED and not waitOnFlip:
            theseKeys = passagemBarra.getKeys(keyList=['space'], waitRelease=False)
            _passagemBarra_allKeys.extend(theseKeys)
            if len(_passagemBarra_allKeys):
                passagemBarra.keys = _passagemBarra_allKeys[-1].name  # just the last key pressed
                passagemBarra.rt = _passagemBarra_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *pergunta* updates
        if pergunta.status == NOT_STARTED and sound_clip.status==FINISHED:
            # keep track of start time/frame for later
            pergunta.frameNStart = frameN  # exact frame index
            pergunta.tStart = t  # local t and not account for scr refresh
            pergunta.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(pergunta, 'tStartRefresh')  # time at next scr refresh
            pergunta.setAutoDraw(True)
        # *ISI* period
        if ISI.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ISI.frameNStart = frameN  # exact frame index
            ISI.tStart = t  # local t and not account for scr refresh
            ISI.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ISI, 'tStartRefresh')  # time at next scr refresh
            ISI.start(3)
        elif ISI.status == STARTED:  # one frame should pass before updating params and completing
            ISI.complete()  # finish the static period
            ISI.tStop = ISI.tStart + 3  # record stop time
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in experimentoComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "experimento"-------
    for thisComponent in experimentoComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    loop_experimento.addData('ouca.started', ouca.tStartRefresh)
    loop_experimento.addData('ouca.stopped', ouca.tStopRefresh)
    sound_clip.stop()  # ensure sound has stopped at end of routine
    loop_experimento.addData('sound_clip.started', sound_clip.tStartRefresh)
    loop_experimento.addData('sound_clip.stopped', sound_clip.tStopRefresh)
    loop_experimento.addData('repetir.started', repetir.tStartRefresh)
    loop_experimento.addData('repetir.stopped', repetir.tStopRefresh)
    loop_experimento.addData('slider.response', slider.getRating())
    loop_experimento.addData('slider.rt', slider.getRT())
    loop_experimento.addData('slider.started', slider.tStartRefresh)
    loop_experimento.addData('slider.stopped', slider.tStopRefresh)
    loop_experimento.addData('passagem.started', passagem.tStartRefresh)
    loop_experimento.addData('passagem.stopped', passagem.tStopRefresh)
    loop_experimento.addData('pergunta.started', pergunta.tStartRefresh)
    loop_experimento.addData('pergunta.stopped', pergunta.tStopRefresh)
    loop_experimento.addData('ISI.started', ISI.tStart)
    loop_experimento.addData('ISI.stopped', ISI.tStop)
    # the Routine "experimento" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'loop_experimento'


# ------Prepare to start Routine "final"-------
continueRoutine = True
routineTimer.add(3.000000)
# update component parameters for each repeat
# keep track of which components have finished
finalComponents = [text_3]
for thisComponent in finalComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
finalClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "final"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = finalClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=finalClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_3* updates
    if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_3.frameNStart = frameN  # exact frame index
        text_3.tStart = t  # local t and not account for scr refresh
        text_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
        text_3.setAutoDraw(True)
    if text_3.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_3.tStartRefresh + 3.0-frameTolerance:
            # keep track of stop time/frame for later
            text_3.tStop = t  # not accounting for scr refresh
            text_3.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_3, 'tStopRefresh')  # time at next scr refresh
            text_3.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in finalComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "final"-------
for thisComponent in finalComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_3.started', text_3.tStartRefresh)
thisExp.addData('text_3.stopped', text_3.tStopRefresh)

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
