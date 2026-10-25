

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>pArt</title>

    <style>
        * {
            box-sizing: border-box;
        }

        body {
            margin: 0;
            min-height: 100vh;
            background: pink;
            font-family: "Press Start 2P", monospace;
            text-align: center;
            color: black;
        }

        h1 {
            font-size: clamp(20px, 4vw, 40px);
            margin: 30px 10px;
        }

        h2 {
            font-size: clamp(16px, 3vw, 24px);
            margin: 25px 10px;
        }

        button {
            font-family: inherit;
            font-size: clamp(10px, 2vw, 16px);
            background: #F9B4D9;
            color: black;
            border: 2px solid #d88bb5;
            padding: 15px;
            cursor: pointer;
        }

        button:hover {
            background: #f6a0ce;
        }

        .screen {
            min-height: 100vh;
            padding: 15px;
        }

        .main-button {
            width: 100%;
            min-height: 100px;
            margin: 12px 0;
        }

        .hidden {
            display: none;
        }

        .back {
            display: block;
            margin: 0 0 15px;
            padding: 10px 18px;
        }

        .canvas-area {
            display: flex;
            justify-content: center;
            align-items: center;
            margin: 20px auto;
            width: 100%;
        }

        canvas {
            background: white;
            width: min(320px, 85vw);
            height: min(320px, 85vw);
            border: 1px solid gray;
            touch-action: none;
            cursor: crosshair;
        }

        .tools {
            display: flex;
            justify-content: center;
            flex-wrap: wrap;
            gap: 10px;
            margin: 15px auto;
        }

        .tools button {
            font-size: 12px;
        }

        input[type="color"] {
            width: 55px;
            height: 45px;
            cursor: pointer;
        }
    </style>
</head>

<body>

    <!-- Welcome screen -->
    <section id="welcome" class="screen">
        <h1>welcome To pArt</h1>

        <button class="main-button" onclick="showStart()">
            Get Started
        </button>
    </section>

    <!-- Start screen -->
    <section id="start" class="screen hidden">
        <button class="back" onclick="showWelcome()">←</button>

        <h1>Now You Can Start</h1>

        <button class="main-button" onclick="showMenu()">
            Use Blank Canvas
        </button>
    </section>

    <!-- Canvas size menu -->
    <section id="menu" class="screen hidden">
        <button class="back" onclick="showStart()">←</button>

        <h2>Good luck &gt;_&lt;</h2>

        <button class="main-button" onclick="openCanvas(16)">
            16x16
        </button>

        <button class="main-button" onclick="openCanvas(32)">
            32x32
        </button>

        <button class="main-button" onclick="openCanvas(64)">
            64x64
        </button>
    </section>

    <!-- Drawing screen -->
    <section id="drawing" class="screen hidden">
        <button class="back" onclick="showMenu()">←</button>

        <h2 id="canvas-title">16x16</h2>

        <div class="tools">
            <label>
                Choose color
                <input type="color" id="colorPicker" value="#000000">
            </label>

            <button onclick="toggleEraser()" id="eraserButton">
                Erase
            </button>
        </div>

        <div class="canvas-area">
            <canvas id="artCanvas" width="320" height="320"></canvas>
        </div>
    </section>

    <script>
        const screens = document.querySelectorAll(".screen");
        const canvas = document.getElementById("artCanvas");
        const ctx = canvas.getContext("2d");
        const colorPicker = document.getElementById("colorPicker");
        const eraserButton = document.getElementById("eraserButton");

        let gridSize = 16;
        let cellSize = 20;
        let currentColor = "#000000";
        let erasing = false;
        let drawing = false;

        function showScreen(id) {
            screens.forEach(screen => {
                screen.classList.add("hidden");
            });

            document.getElementById(id).classList.remove("hidden");
        }

        function showWelcome() {
            showScreen("welcome");
        }

        function showStart() {
            showScreen("start");
        }

        function showMenu() {
            showScreen("menu");
        }

        function openCanvas(size) {
            gridSize = size;
            cellSize = 320 / gridSize;

            document.getElementById("canvas-title").textContent =
                size + "x" + size;

            erasing = false;
            eraserButton.textContent = "Erase";
            currentColor = colorPicker.value;

            showScreen("drawing");
            drawGrid();
        }

        function drawGrid() {
            ctx.fillStyle = "white";
            ctx.fillRect(0, 0, 320, 320);

            ctx.strokeStyle = "lightgray";
            ctx.lineWidth = 1;

            for (let i = 0; i <= gridSize; i++) {
                const position = i * cellSize;

                ctx.beginPath();
                ctx.moveTo(position, 0);
                ctx.lineTo(position, 320);
                ctx.stroke();

                ctx.beginPath();
                ctx.moveTo(0, position);
                ctx.lineTo(320, position);
                ctx.stroke();
            }
        }

        colorPicker.addEventListener("input", function () {
            currentColor = colorPicker.value;
            erasing = false;
            eraserButton.textContent = "Erase";
        });

        function toggleEraser() {
            erasing = !erasing;

            eraserButton.textContent =
                erasing ? "Stop erasing" : "Erase";
        }

        function draw(event) {
            if (!drawing) return;

            const rect = canvas.getBoundingClientRect();

            const x = (event.clientX - rect.left) *
                (canvas.width / rect.width);

            const y = (event.clientY - rect.top) *
                (canvas.height / rect.height);

            if (x < 0 || x >= 320 || y < 0 || y >= 320) return;

            const cellX = Math.floor(x / cellSize) * cellSize;
            const cellY = Math.floor(y / cellSize) * cellSize;

            ctx.fillStyle = erasing ? "white" : currentColor;

            ctx.fillRect(
                cellX,
                cellY,
                cellSize,
                cellSize
            );

            ctx.strokeStyle = "lightgray";
            ctx.lineWidth = 1;

            ctx.strokeRect(
                cellX,
                cellY,
                cellSize,
                cellSize
            );
        }

        canvas.addEventListener("pointerdown", function (event) {
            drawing = true;
            canvas.setPointerCapture(event.pointerId);
            draw(event);
        });

        canvas.addEventListener("pointermove", draw);

        canvas.addEventListener("pointerup", function () {
            drawing = false;
        });

        canvas.addEventListener("pointercancel", function () {
            drawing = false;
        });

        showWelcome();
    </script>

</body>
</html>
