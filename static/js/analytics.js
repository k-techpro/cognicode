const startTimeStored = localStorage.getItem("startTime");
const typingCountStored = localStorage.getItem("typingCount");
const problemsSolvedStored = localStorage.getItem("problemsSolved");
const totalAttemptsStored = localStorage.getItem("totalAttempts");
const correctAttemptsStored = localStorage.getItem("correctAttempts");

const now = Date.now();
const startTime = startTimeStored ? parseInt(startTimeStored) : now;
const typingCount = typingCountStored ? parseInt(typingCountStored) : 0;
const problemsSolved = problemsSolvedStored ? parseInt(problemsSolvedStored) : 0;
const totalAttempts = totalAttemptsStored ? parseInt(totalAttemptsStored) : 0;
const correctAttempts = correctAttemptsStored ? parseInt(correctAttemptsStored) : 0;

const totalSeconds = Math.max(1, Math.floor((now - startTime) / 1000));
const totalMinutes = Math.floor(totalSeconds / 60);

const typingSpeed = Math.floor((typingCount / totalSeconds) * 60) || 0;
const focusScore = Math.min(100, Math.max(20, typingSpeed));
const accuracyScore = totalAttempts > 0 ? Math.round((correctAttempts / totalAttempts) * 100) : 0;
const productivityScore = Math.min(100, Math.round((focusScore * 0.4) + (accuracyScore * 0.4) + (Math.min(problemsSolved * 10, 100) * 0.2)));

document.getElementById("timeSpent").innerText = `${totalMinutes} min`;
document.getElementById("typingSpeed").innerText = `${typingSpeed} CPM`;
document.getElementById("focusScore").innerText = `${focusScore}%`;
document.getElementById("problemsSolved").innerText = problemsSolved;
document.getElementById("accuracyScore").innerText = `${accuracyScore}%`;
document.getElementById("productivityScore").innerText = `${productivityScore}%`;

let learningPattern = "Balanced Learner";
let strongArea = "Problem Persistence";
let weakArea = "Typing Consistency";
let engagementLevel = "Moderate";

if (focusScore >= 70 && accuracyScore >= 70) {
  learningPattern = "Focused Performer";
  strongArea = "Coding Accuracy";
  weakArea = "Advanced Challenge Exposure";
  engagementLevel = "High";
} else if (focusScore < 40) {
  learningPattern = "Distracted Learner";
  strongArea = "Attempt Willingness";
  weakArea = "Focus and Typing Consistency";
  engagementLevel = "Low";
} else if (problemsSolved >= 5) {
  learningPattern = "Persistent Solver";
  strongArea = "Problem Completion";
  weakArea = "Speed Optimization";
  engagementLevel = "High";
}

document.getElementById("learningPattern").innerText = learningPattern;
document.getElementById("strongArea").innerText = strongArea;
document.getElementById("weakArea").innerText = weakArea;
document.getElementById("engagementLevel").innerText = engagementLevel;

const dailyLabels = window.LABELS || [];
const dailyTime = window.DATA || [];

const avgDaily = Math.round(dailyTime.reduce((a, b) => a + b, 0) / dailyTime.length);

new Chart(document.getElementById("dailyTimeChart"), {
  type: "bar",
  data: {
    labels: dailyLabels,
    datasets: [{
      label: "Time Spent (min)",
      data: dailyTime
    }]
  },
  options: {
    responsive: true,
    plugins: {
      legend: {
        labels: { color: "#eaf4ff" }
      }
    },
    scales: {
      x: {
        ticks: { color: "#c4d3ea" },
        grid: { color: "rgba(255,255,255,0.08)" }
      },
      y: {
        ticks: { color: "#c4d3ea" },
        grid: { color: "rgba(255,255,255,0.08)" }
      }
    }
  }
});

new Chart(document.getElementById("timeComparisonChart"), {
  type: "line",
  data: {
    labels: ["Total Time", "Daily Average"],
    datasets: [{
      label: "Minutes",
      data: [totalMinutes, avgDaily],
      fill: false,
      tension: 0.3
    }]
  },
  options: {
    responsive: true,
    plugins: {
      legend: {
        labels: { color: "#eaf4ff" }
      }
    },
    scales: {
      x: {
        ticks: { color: "#c4d3ea" },
        grid: { color: "rgba(255,255,255,0.08)" }
      },
      y: {
        ticks: { color: "#c4d3ea" },
        grid: { color: "rgba(255,255,255,0.08)" }
      }
    }
  }
});