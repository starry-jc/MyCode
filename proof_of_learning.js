// This app was made as my Proof of Learning project for AP Computer Science Principles, Spring 2026.
//  The app is inspired by the hit-game Wordle on New York Times: https://www.nytimes.com/games/wordle/index.html
//  and made through https://code.org. The app uses one of their databases called "Wordle". 
// The actual app can be accessed here: https://studio.code.org/projects/applab/1597dcd8-cc1b-4c70-ac86-168d8c726350
// This file just contains the code.

// Image Credits:
//  homeScreen background image found from: https://www.publicdomainpictures.net/en/view-image.php?image=418773&picture=star-paper-background-pattern
//  restartButton image found from: https://publicdomainvectors.org/en/free-clipart/Reboot-symbol/59316.html
//    background removed through https://www.remove.bg/
//  shootingStarDecor image found from: https://www.wannapik.com/vectors/42164
//    background image removed through https://www.remove.bg/
//  notebookDecor image found from: https://www.wannapik.com/vectors/28660
//    background image reoved through https://www.remove.bg/

// Variables/Lists

// Importing data from datasets
var validStardleGuessList = getColumn("Wordle", "validWordleGuess");
var validStardleAnswerList = getColumn("Wordle", "validWordleAnswer");

// Creates a filtered list of validStardleAnswerList
var filteredStardleAnswerList = [];

// Creates an empty string that will later hold a random word from
//  validStardleAnswerList
var correctWord = '';

// Creates an empty string that will later hold the guess word that is
//  inputted by the user.
var starWord = "";

// Creates an empty list that will later hold all of the guesses
//  made by the user.
var guessHistory = [];

// Creates a number variable that will be updated whenever the user
//  makes a guess.
var numGuesses = 0;

// Creates a  number variable that will be updated when the user
//  makes a guess, but is the value that will stay the same when
//  the user interacts with the slider.
var maxGuesses = 0;

// Creates a string variable that will hold a default the default
//  guessSlider message.
var guessSliderMessage = "Revert to Guess No.: ";


// Filters validStardleAnswerList
stardleAnswerFilter();

// Resets the game to the default
resetGame();


// Event Handlers

// Purpose: Reviews the guess and determines which characters
//  of the word match the correct word (determined randomly).
// Function: Assigns the variable starWord equal to the text
//  inputted by the user.
//  Hides the directions directionx box.
//  Empties the input box.
//  Calls the inputGuess variable, passing starWord as the
//  argument.
onEvent("guessButton", "click", function() {
  starWord = getText("guessInputBox").toLowerCase();
  
  hideElement("gameDirectionsOrFinish");
  setText("guessInputBox", '');
  
  inputGuess(starWord);
});

// Purpose: If the user moves the slider to the left,
//  indicates that they wish to undo a guess.
//  If the user moves the slider to the right (if applicable),
//  indicates that they wish to redo a guess.
// Function: Creates a local variable numRevert and assigns
//  it to the value of the guessSlider after the change.
//  If numRevert is less than or equal to 4 (in context: 4
//  attempts), set the text of guessSlideLabel (text below
//  the slider) to the number from the slider plus 1 (represents
//  the row). This filters out any attempts greater than 4
//  (because when the user makes their fifth guess, it will
//  indicate losing).
//    If numRevert (slider value) is less than numGuesses
//    (current number of guesses), this will imply an undo guess.
//    Calls the function undoGuess, passing the parameter
//    numRevert.
//    If numRevert is greater than numGuesses, this will imply
//    a redo guess.
//    Calls the function redoGuess, passing the parameter
//    numRevert.
onEvent("guessSlider", "change", function() {
  var numRevert = getNumber("guessSlider");
  
  if (numRevert <= 4) {
    setText("guessSlideLabel", guessSliderMessage + (getNumber("guessSlider") + 1));
    
    if (numRevert < numGuesses) {
      undoGuess(numRevert);
    } else if (numRevert > numGuesses) {
      redoGuess(numRevert);
    }
  }
});

// Purpose: When clicked, the entire app will reset just as it
//  was when the app is started for the first time.
// Function: Calls the resetGame function.
onEvent("restartButton", "click", function() {
  resetGame();
});



// Functions

// Purpose: When called, filters all of the non-null
//  elements from the original list into the filtered
//  list.
// Function: empties the filteredStardleAnswerList.
//  Using filter, traverses through validStardleAnswerList:
//    If the element at index i of validStardleAnswerList
//    is not a null element, append the item into filtered-
//    StardleAnswerList.
function stardleAnswerFilter() {
  filteredStardleAnswerList = [];
  
  
  for (var i = 0; i < validStardleAnswerList.length; i++) {
    if (validStardleAnswerList[i] != null) {
      appendItem(filteredStardleAnswerList, validStardleAnswerList[i]);
    }
  }
}

// (Buckle up this is gonna be a long one.)
// Purpose: When called, it will first check to
//  make sure your guess is valid. If it is, it will
//  uppercase it, and if the current number of guesses
//  is greater than the maximum number of guesses,
//  it will add the item into the guessHistory list.
//  Otherwise, it will replace the element in the list
//  at the current guess minus 1 with the guess.
//  While the current number of guesses is less than or
//  equal to 5, it will basically go through a process where
//  it compares every guess with the correct word in each
//  row. If they are characters in the same place, it will
//  be marked green; if they are the correct characters but
//  not in the same place, it will be marked yellow; and
//  all wrong letters will be grayed out.
//  If the guess matches the correct word, then the game will
//  end and a winner message will display and end the function.
//  If the number of guesses reaches 5, but no correct guess
//  has been found, then the game will end and a losing message
//  will be displayed with the correct word, and the function
//  will end.
//  If the guess is not considered valid, then it will display
//  an error message display and reset the slider so that it
//  won't count the invalid guess and the function will end.
//  If the current number of guesses is greater than the 
//  maximum number of guesses, the max number will be updated
//  to the current number of Guesses.
//  Finally, the game directions will be hidden and the slider
//  will be updated accordingly.
// Function: Assigns a local variable validGuess to false.
//  numGuesses will add 1, and guessSlideLabel will be updated
//  to hvae the row number.
//  Using reduce, traverses through validStardleGuessList:
//    If the argument passed through the parameter guess is the same
//    as the element at index i of validStardleGuessList OR guess
//    is the same as the element at index i of filteredStardleAnswer-
//    List, then validGuess will be assigned to true and guess
//    will be uppercased.
//      If numGuesses (current number of guesses) is greater than
//      maxGuesses (maximum number of guesses), append the item into
//      guessHistory.
//      Otherwise, the element at index numGuesses minus 1 will be replaced
//      with guess.
//    If numGuesses is less than or equal to 5:
//      Creates a local variable remainingLetters and assigns it to
//      correctWord (random word from filteredStardleAnswerList).
//      Traverses through each character of guess (for green characters):
//        Sets the property of starGuess_ (with _ being the number
//        of the character placement in guess) hidden to be false.
//        Sets the text of starGuess_ to the each letter in guess.
//        This represents each starGuess in a single row, and will be
//        updated for each row in the game.
//          If the lowercase character j of guess is equal to the character
//          j of correctWord, sets the icon color of starBox_ to green,
//          and replaces said character in remainingLetters to an underscore.
//          This is what tells the game that the specific character was used
//          for green, and if there was another of the same letter in a different
//          place, it wouldn't be marked yellow because the green traversal does
//          it first.
//      Traverses through each character of guess (this time for yellow words):
//        If the character k at guess is not the same as character k in correct-
//        Word (which filters out any of the same characters that were addressed
//        in the previous traversal):
//          If remainingLetters (correctWord without green-boxed characters) includes
//          a character k from guess, then creates a local variable index
//          and assigns it to the index of a character k in remainingLetters.
//          Sets the icon color of starGuess_ to yellow, and replaces the
//          character in remainingLetters to an underscore.
//          Otherwise, sets the icon color to a darker grey.
//    If guess is equal to correctWord, then sets the text of gameDirections-
//    orFinish to a "You Win!" message and adjusts some formatting of the textBox.
//    Shows restartButton and gameDirectionsorFinish. Ends the function.
//    If numGuesses is equal to 5 (and guess is not equal to correctWord),
//    indicates that the user has lost the game. Sets the text of
//    gameDirectionsOrFinish to a "You lose" message, along with the correct
//    word. Shows restartButton and gameDirectionsOrFinish. Ends the function.
//  If validGuess is false, then subtracts 1 from numGuesses.
//  Ensures that the max value of the slider is the max number of guesses, and
//  the value of the slider is the current number of guesses. Updates
//  guessSlideLabel to the current number of guesses.
//  Sets the text of gameDirectionsOrFinish to "Invalid guess", formats some
//  colors, and shows gameDirectionsOrFinish. Ends the function.
//  If none of the conditions above are true, that implies that all guesses
//  were valid and the user has not found the correct word yet.
//  If numGuesses is greater than maxGuesses, then updates the value
//  of maxGuesses to be equal to numGuesses.
//  Hides gameDirectionsOrFinish.
//  Updates the properties of the slider and its message.
function inputGuess(guess) {
  var validGuess = false;
  
  numGuesses += 1;
  setText("guessSlideLabel", guessSliderMessage + (getNumber("guessSlider") + 1));
  
  for (var i = 0; i < validStardleGuessList.length; i++) {
    if (guess == validStardleGuessList[i]
          || guess == filteredStardleAnswerList[i]) {
      validGuess = true;
      guess = guess.toUpperCase();
      
      if (numGuesses > maxGuesses) {
        appendItem(guessHistory, guess); 
      } else {
        guessHistory[numGuesses-1] = guess;
      }
        
      if (numGuesses <= 5) {
        var remainingLetters = correctWord.toLowerCase();
        
        for (var j = 1; j < guess.length+1; j++) {
          setProperty("starGuess" + (j+(5*(numGuesses-1))), "hidden", false);
          setText("starGuess" + (j+(5*(numGuesses-1))), guess.substring(j-1, j));
          
          if (guess.toLowerCase().substring(j-1, j) == correctWord.substring(j-1, j)) {
            setProperty("starBox" + (j+(5*(numGuesses-1))), "icon-color", "#b8dc94");
            remainingLetters = remainingLetters.substring(0,j-1) +
                                  "-" + remainingLetters.substring(j);
          }
        } 
        
        for (var k = 1; k < guess.length+1; k++) {
          if (guess.toLowerCase().substring(k-1, k) != correctWord.substring(k-1, k)) {
            if (remainingLetters.includes(guess.toLowerCase().substring(k-1, k))) {
              var index = remainingLetters.indexOf(guess.toLowerCase().substring(k-1, k));
              
              setProperty("starBox" + (k+(5*(numGuesses-1))), "icon-color", "#f2cd72");
              remainingLetters = remainingLetters.substring(0, index) +
                                    "-" + remainingLetters.substring(index + 1);
            } else {
              setProperty("starBox" + (k+(5*(numGuesses-1))), "icon-color", "#4d4949");
            }
          }
        }
      } 
      
      if (guess.toLowerCase() == correctWord) {
        setText("gameDirectionsOrFinish", "You win! Congrats! Play again?");
        setProperty("gameDirectionsOrFinish", "text-color", "#6FE71F");
        setProperty("gameDirectionsOrFinish", "width", 245);
        
        showElement("restartButton");
        showElement("gameDirectionsOrFinish");
        
        return;
      }
      
      if (numGuesses == 5) {
        setText("gameDirectionsOrFinish", "You lose. The word was \"" + correctWord + "\".");
        setProperty("gameDirectionsOrFinish", "text-color", "#BE2727");
        setProperty("gameDirectionsOrFinish", "width", 245);
        
        showElement("restartButton");
        showElement("gameDirectionsOrFinish");
        
        return;
      }
      
    }
  }
  
  
  if (validGuess == false) {
    numGuesses -= 1;
    
    setProperty("guessSlider", "max", maxGuesses);
    setProperty("guessSlider", "value", numGuesses);
    setText("guessSlideLabel", guessSliderMessage + (getNumber("guessSlider") + 1));
    
    setText("gameDirectionsOrFinish", "Not a valid guess.");
    setProperty("gameDirectionsOrFinish", "text-color", "#BE2727");
    showElement("gameDirectionsOrFinish");
    
    return;
  }
  
  if (numGuesses > maxGuesses) {
    maxGuesses = numGuesses;
  } 
  
  hideElement("gameDirectionsOrFinish");
  
  setProperty("guessSlider", "max", maxGuesses);
  setProperty("guessSlider", "value", numGuesses);
  setText("guessSlideLabel", guessSliderMessage + (getNumber("guessSlider") + 1));
}

// Purpose: When called, the most recent guess(es) will become
//  invisible. The number of guesses depends on how far back the
//  user drags the slider.
// Function: While numGuesses (current number of guesses) is greater
//  than the argument passed through the parameter step:
//    Uses a for loop that starts at 1 and ends at 5:
//      Hides the element of starGuess_ (_ being replaced with the number i)
//      to represent each character from one row.
//      Updates the color to be a lighter gray, representing a blank space.
//    numGuesses will subtract 1 in value.
function undoGuess(step) {
  while (numGuesses > step) {
    for (var i = 1; i <= 5; i++) {
      hideElement("starGuess" + (i+(5*(numGuesses-1))));
      setProperty("starBox" + (i+(5*(numGuesses-1))), "icon-color", "#969494");
    }
    
    numGuesses -= 1;
  }
}

// Purpose: When called, the user will revert to previous guesses
//  they have already made. Those guesses, that were originally hidden
//  because the user previously undid a guess, will unhide and the correct
//  character, placement, and color will stay the same as before the user
//  undid their guess.
// Function: While numGuesses is less than the argument passed through the
//  parameter step:
//    Creates a local variable prevGuesses which represents the
//    element of index numGuesses in the list guessHistory.
//    The following actions are very similar to the actions in inputGuess
//    under the if statement that checks if numGuesses is less than 5,
//    so the following comments will be pretty much copied and pasted.
//    (I'll surround brackets around the parts that are different.)
//      Creates a local variable remainingLetters and assigns it to
//      correctWord (random word from filteredStardleAnswerList).
//      [Uses a for loop that starts at 1 and ends at 5] (for green characters):
//        Sets the property of starGuess_ (with _ being the number
//        of the character placement in guess) hidden to be false.
//        Sets the text of starGuess_ to the each letter in guess.
//        This represents each starGuess in a single row, and will be
//        updated for each row in the game.
//          If the lowercase character [i] of [prevGuess] is equal to the character
//          [i] of correctWord, sets the icon color of starBox_ to green,
//          and replaces said character in remainingLetters to an underscore.
//          This is what tells the game that the specific character was used
//          for green, and if there was another of the same letter in a different
//          place, it wouldn't be marked yellow because the green traversal does
//          it first.
//      Traverses through each character of [prevGuess] (this time for yellow words):
//        If the character k at [prevGuess] is not the same as character k in correct-
//        Word (which filters out any of the same characters that were addressed
//        in the previous traversal):
//          If remainingLetters (correctWord without green-boxed characters) includes
//          a character k from [prevGuess], then creates a local variable index
//          and assigns it to the index of a character k in remainingLetters.
//          Sets the icon color of starGuess_ to yellow, and replaces the
//          character in remainingLetters to an underscore.
//          Otherwise, sets the icon color to a darker grey.
//    numGuesses will add 1 in value.
function redoGuess(step) {
  while (numGuesses < step) {
    var prevGuess = guessHistory[numGuesses];
    var remainingLetters = correctWord.toLowerCase();
        
    for (var i = 1; i <= 5; i++) {
      showElement("starGuess" + (i+(5*(numGuesses))));
      
      if (prevGuess.toLowerCase().substring(i-1, i) == correctWord.substring(i-1, i)) {
        setProperty("starBox" + (i+(5*(numGuesses))), "icon-color", "#b8dc94");
        remainingLetters = remainingLetters.substring(0,i-1) +
                              "-" + remainingLetters.substring(i);
      }
    } 
    
    for (var k = 1; k <= 5; k++) {
      if (prevGuess.toLowerCase().substring(k-1, k) != correctWord.substring(k-1, k)) {
        if (remainingLetters.includes(prevGuess.toLowerCase().substring(k-1, k))) {
          var index = remainingLetters.indexOf(prevGuess.toLowerCase().substring(k-1, k));
          
          setProperty("starBox" + (k+(5*numGuesses)), "icon-color", "#f2cd72");
          remainingLetters = remainingLetters.substring(0, index) +
                                "-" + remainingLetters.substring(index + 1);
        } else {
          setProperty("starBox" + (k+(5*numGuesses)), "icon-color", "#4d4949");
        }
      }
    }
    
    numGuesses += 1;
  }
  
}

// Purpose: When called, it will reset the game to its default
//  screen. It hides all of the star guesses, hides the restart
//  button, brings the directions back out, and resets the slider.
// Function: Creates a local variable called starGuessNum and sets
//  equal to 1. This variable represents the value of each
//  starGuess.
//  While starGuessNum is less than or equal to 25:
//    Hides starGuess_ (with _ represented by starGuessNum) and sets
//    the icon color of starBox_ (same thing) to a default light gray
//    color that represents a blank space.
//    starGuessNum increments by 1.
//  Sets the text of gameDirectionsOrFinish to a default message
//  with the directions, and formats the text color and width.
//  Hides restartButton.
//  Resets the values of numGuesses and maxGuesses by setting them
//  equal to 0.
//  Re-randomizes a correctWord for next gameplay.
//  Empties guessHistory list.
//  Resets the slider by setting the max and value equal to 0,
//  and sets the text of guessSlideLabel to the default guessSlider-
//  Message.
function resetGame() {
  var starGuessNum = 1;
  
  while (starGuessNum <= 25) {
    setProperty("starGuess" + starGuessNum, "hidden", true);
    setProperty("starBox" + starGuessNum, "icon-color", "#969494");
    
    starGuessNum++;
  }
  
  setText("gameDirectionsOrFinish", "Enter a 5 letter word.");
  setProperty("gameDirectionsOrFinish", "text-color", "#ecc47e"); 
  setProperty("gameDirectionsOrFinish", "width", 305);
  
  hideElement("restartButton");
  
  numGuesses = 0;
  maxGuesses = 0;
  correctWord = filteredStardleAnswerList[
                  randomNumber(0,filteredStardleAnswerList.length-1)];
  guessHistory = [];
                  
  setProperty("guessSlider", "max", 0);
  setProperty("guessSlider", "value", 0);
  setText("guessSlideLabel", guessSliderMessage);
}

// Color codes:
//  correct char, wrong place: #f2cd72
//  correct char, correct place: #b8dc94
//  wrong char, wrong place: #4d4949
//  blank space: #969494

//  error/lose msg: #BE2727
//  default msg: #ecc47e
//  win msg: #6FE71F
