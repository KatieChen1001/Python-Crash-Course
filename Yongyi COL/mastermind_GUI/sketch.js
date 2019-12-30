// draw 8 balls of different color
// randomly choose 4 out of 8 colors store
// click ball, highlight ball, get ball color
// click square
// onClick Check:
// - check if ball clicked, yes: get ball colors, ballSelected to true
// - check if square clicked, if ballSelected is true, draw ball in square center

// BONUS FEATURES:
// 1. Add timer
// 2. Add game instructions
// 3. Make everything responsive
// 4. Add give up button for each round

// TODO:

let canvasWidth = 800;
let canvasHeight = 500;
let canvasSpacing = 100;
let backgroundColor = 250;
let ballDiameter = 40;
let ballRadius = ballDiameter / 2;
let ballSpacing = ballRadius / 2;

// let buttonCheck = createButton("Check");

function setup() {
  createCanvas(canvasWidth, canvasHeight);
}

// draw the user input grid
let gridLeftX = 7 * ballRadius;
let gridLeftY = canvasSpacing - ballSpacing;
let gridSquare = ballDiameter + ballRadius;
function drawGrid() {
  stroke("rgba(0,0,0,0.25)");
  strokeWeight(2);
  for (let i = 0; i < 10; i++) {
    for (let j = 0; j < 4; j++) {
      fill(color("rgba(255, 255, 255, 0.5)"));
      rect(
        gridLeftX + i * gridSquare,
        gridLeftY + j * gridSquare,
        gridSquare,
        gridSquare
      );
    }
  }
}

class Ball {
  constructor(x, y, ballDiameter, ballColor) {
    this.x = x;
    this.y = y;
    this.diameter = ballDiameter;
    this.ballColor = ballColor;
    this.ballSelected = false;
  }

  draw() {
    noStroke();
    fill(color(this.ballColor));
    circle(this.x, this.y, this.diameter);
  }

  update() {
    this.x = mouseX;
    this.y = mouseY;
  }

  xloc() {
    return this.x;
  }

  yloc() {
    return this.y;
  }

  isBallClicked() {
    let rad = this.diameter / 2;
    let ballRangeLeft = this.x - rad;
    let ballRangeRight = this.x + rad;
    let ballRangeTop = this.y - rad;
    let ballRangeBottom = this.y + rad;
    if (
      mouseX < ballRangeRight &&
      mouseX > ballRangeLeft &&
      mouseY < ballRangeBottom &&
      mouseY > ballRangeTop
    ) {
      print("");
      return this.ballColor;
    } else {
      return undefined;
    }
  }
}

let balls = [];

//   ball palette display
let ballColors = [
  "#000000",
  "#55415f",
  "#646964",
  "#d77355",
  "#508cd7",
  "#64b964",
  "#e6c86e",
  "#dcf5ff"
]; // color() takes hex code in string type
function generateBallPalette() {
  let j = 0;
  for (let i = 1; i < 13; i = i + 3) {
    //   1st column of balls
    let ball1stCol = new Ball(
      ballDiameter,
      canvasSpacing + i * ballRadius,
      ballDiameter,
      ballColors[j]
    );
    balls.push(ball1stCol);
    j++;
    //   2nd column of balls
    let ball2ndCol = new Ball(
      5 * ballRadius,
      canvasSpacing + i * ballRadius,
      ballDiameter,
      ballColors[j]
    );
    balls.push(ball2ndCol);
    j++;
  }
}

// Display scoreboard for each round
function scoreBoard() {}

let ballHovered = false;
let ballSelected = false;

let userGuess = [];
let locked = false;

function mouseClicked() {
  let selectedBallColor;
  if (!locked) {
    for (let i = 0; i < balls.length; i++) {
      if (balls[i].isBallClicked() != undefined) {
        selectedBallColor = balls[i].isBallClicked();
        print(typeof selectedBallColor);
        print(selectedBallColor);
        break;
      }
    }
    let selectedBall = new Ball(
      mouseX,
      mouseY,
      ballDiameter,
      selectedBallColor
    );
    userGuess.push(selectedBall);
    locked = !locked;
  } else {
    locked = !locked;
  }
}

function draw() {
  // ==== Setup the basics ==== //
  background(backgroundColor);
  generateBallPalette();
  for (let i = 0; i < balls.length; i++) {
    balls[i].draw();
  }
  drawGrid();
  // ==== draw user selected balls ==== //
  for (let i = 0; i < userGuess.length; i++) {
    userGuess[i].draw();
    print(userGuess[i].xloc());
    if (locked) {
      userGuess[i].update();
    }
  }
}
