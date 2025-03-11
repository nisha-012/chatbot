let selectedTopicId = null;

// Select Topic and Show Question Button
function selectTopic(topicId, topicName) {
    selectedTopicId = topicId;
    document.getElementById("selected-topic").innerText = `Selected Topic: ${topicName}`;
    document.getElementById("selected-topic").style.display = "block";
    document.getElementById("choose-question-btn").style.display = "block";
}

// Open Modal and Fetch Questions
function openQuestionModal() {
    if (!selectedTopicId) return alert("Please select a topic first!");

    // Show loading spinner
    document.getElementById("loadingSpinner").style.display = "flex";
    document.getElementById("questions-list").innerHTML = "";

    fetch(`/get-questions/${selectedTopicId}/`)
        .then(response => response.json())
        .then(data => {
            console.log("Received questions:", data);  // Debugging

            // Hide loading spinner
            document.getElementById("loadingSpinner").style.display = "none";

            let questionList = document.getElementById("questions-list");
            questionList.innerHTML = "";

            if (data.questions.length === 0) {
                questionList.innerHTML = "<p>No questions available for this topic.</p>";
                return;
            }

            data.questions.forEach(q => {
                let btn = document.createElement("button");
                btn.classList.add("question-btn");
                btn.innerText = q.question_text;
                btn.onclick = () => selectQuestion(q.question_text, q.answer_text, q.pdf_link);
                questionList.appendChild(btn);
            });

            // Add search functionality
            document.getElementById("searchQuestion").addEventListener("input", (e) => {
                const searchTerm = e.target.value.toLowerCase();
                const questions = document.querySelectorAll(".question-btn");
                questions.forEach(question => {
                    const questionText = question.innerText.toLowerCase();
                    if (questionText.includes(searchTerm)) {
                        question.style.display = "block";
                    } else {
                        question.style.display = "none";
                    }
                });
            });
        })
        .catch(error => {
            console.error("Error fetching questions:", error);
            document.getElementById("loadingSpinner").style.display = "none";
            document.getElementById("questions-list").innerHTML = "<p>Failed to load questions. Please try again.</p>";
        });

    document.getElementById("questionModal").style.display = "block";
}

// Close Modal
function closeModal() {
    document.getElementById("questionModal").style.display = "none";
}

// Select Question and Display Chat
function selectQuestion(question, answer, pdfLink) {
    closeModal();
    
    let chatBox = document.getElementById("chat-box");

    // Add user question (left side)
    chatBox.innerHTML += `
        <div class="chat-message user-message" style="animation: slideInDown 0.5s ease;">
            <div class="message-content">
                <img src="${staticUrls.userAvatar}" alt="User Avatar" class="avatar">
                <div class="message-text">
                    <p>${question}</p>
                    <span class="timestamp">${new Date().toLocaleTimeString()}</span>
                </div>
            </div>
        </div>
    `;

    // Add bot answer (right side)
    let answerHTML = `
        <div class="chat-message bot-message" style="animation: slideInUp 0.5s ease;">
            <div class="message-content">
                <img src="${staticUrls.botAvatar}" alt="Bot Avatar" class="avatar">
                <div class="message-text">
                    <p>${answer}</p>
    `;
    
    // If there's a PDF link, add it below the answer
    if (pdfLink) {
        answerHTML += `
            <br>
            <a href="${pdfLink}" target="_blank" class="pdf-link">
                <i class="fas fa-file-pdf"></i> View PDF
            </a>
        `;
    }

    answerHTML += `
                    <span class="timestamp">${new Date().toLocaleTimeString()}</span>
                </div>
            </div>
        </div>
    `;
    chatBox.innerHTML += answerHTML;

    // Add options to choose another question or change topic
    chatBox.innerHTML += `
        <button class="btn-choose-question" onclick="openQuestionModal()" style="animation: fadeIn 0.5s ease;">Choose Another Question</button>
        <button class="topic-btn" onclick="location.reload()" style="animation: fadeIn 0.5s ease;">Change Topic</button>
    `;

    // Scroll to the bottom of the chat box
    chatBox.scrollTop = chatBox.scrollHeight;
}