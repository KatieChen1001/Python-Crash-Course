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
// 3. Make everything responsive

// TODO:

let canvasWidth = 800;
let canvasHeight = 500;
let canvasSpacing = 100;
let backgroundColor = 250;
let ballDiameter = 40;
let ballRadius = ballDiameter / 2;
let ballSpacing = ballRadius / 2;

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
    this.ballHovered = false;
  }

  draw() {
    noStroke();
    fill(color(this.ballColor));
    circle(this.x, this.y, this.diameter);
  }

  isBallHovered() {
    // check which ball the mouse is hovering over
    // changed the hovered ball stroke to red
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
      strokeWeight(2);
      stroke("red");
      fill(color(this.ballColor));
      circle(this.x, this.y, this.diameter);
      this.ballHovered = true;
    } else {
      noStroke();
      fill(color(this.ballColor));
      circle(this.x, this.y, this.diameter);
      this.ballHovered = false;
    }
  }

  isBallClicked(ballHovered) {
    // check which ball the mouse is hovering over
    // changed the hovered ball stroke to red
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
      if (ballHovered) {
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

let ballHovered = false;
let ballSelected = false;
let currentSelectedBall;

function mouseClicked() {
  // press once to select ball
  for (let i = 0; i < balls.length; i++) {
    let rad = ballDiameter / 2;
    let ballRangeLeft = balls[i].x - rad;
    let ballRangeRight = balls[i].x + rad;
    let ballRangeTop = balls[i].y - rad;
    let ballRangeBottom = balls[i].y + rad;
    if (
      mouseX < ballRangeRight &&
      mouseX > ballRangeLeft &&
      mouseY < ballRangeBottom &&
      mouseY > ballRangeTop
    ) {
      ballSelected = true;
      let selectedBall = new Ball(
        mouseX,
        mouseY,
        ballDiameter,
        balls[i].ballColor
      );
      print("somthign");
      currentSelectedBall = selectedBall;
      print(currentSelectedBall);
    }
  }
}

function mouseDragged() {
  if (ballSelected) {
    currentSelectedBall.x = mouseX;
    currentSelectedBall.y = mouseY;
  }
}

function draw() {
  background(backgroundColor);
  generateBallPalette();
  for (let i = 0; i < balls.length; i++) {
    balls[i].draw();
  }
  drawGrid();
  if (ballSelected) {
    currentSelectedBall.draw();
  }
}
// press again to deselect ball
// ballSelected = !ballSelected;
// selectedBall.x = mouseX;
// selectedBall.y = mouseY;
// print(selectedBall.x);

//

//
// function mouseClicked() {}
