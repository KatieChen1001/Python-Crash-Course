// draw 8 balls of different color
// randomly choose 4 out of 8 colors store
// each ball will be a class
// every click generates a new ball object
// mousePressed() choose a ball
// mouseDragged() ball follow curse
// mouseClicked() draw ball at location (confine it to grid)

// BONUS FEATURES:
// 1. Add timer
// 2. Add game instructions

// TODO:

let canvasWidth = 800;
let canvasHeight = 500;
let canvasSpacing = 100;
let backgroundColor = 250;
// Ball radius equals to 10% of canvas width
let ballDiameter = 40;
let ballRadius = ballDiameter / 2;
let ballSpacing = ballRadius / 2;

let ballSelected = false;

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
  }

  draw() {
    noStroke();
    fill(color(this.ballColor));
    circle(this.x, this.y, this.diameter);
  }

  isBallClicked(ballSelected) {
    // check which ball mouse is hovering over
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
      // set the clicked ball stroke to red based on whether the user clicked the ball or not
      if (ballSelected) {
        strokeWeight(2);
        stroke("red");
        fill(color(this.ballColor));
        circle(this.x, this.y, this.diameter);
      } else {
        noStroke();
        fill(color(this.ballColor));
        circle(this.x, this.y, this.diameter);
      }
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

let selectedBall;

function draw() {
  background(backgroundColor);
  generateBallPalette();
  for (let i = 0; i < balls.length; i++) {
    balls[i].draw();
  }
  drawGrid();
  // iterate through ball position in ball palette
  for (let i = 0; i < balls.length; i++) {
    balls[i].isBallClicked(ballSelected);
    selectedBall = new Ball(
      mouseX,
      mouseY,
      balls[i].diameter,
      balls[i].ballColor
    );
  }
  selectedBall.draw();
}

function mousePressed() {
  // press once to select ball
  // press again to deselect ball
  ballSelected = !ballSelected;
  selectedBall.x = mouseX;
  selectedBall.y = mouseY;
  print(selectedBall.x);
}
//
function mouseDragged() {
  selectedBall.x = mouseX;
  selectedBall.y = mouseY;
}
