import React, { useState, useEffect, useRef } from 'react';
import axios from 'axios';
import './ChatPage.css';
import Loader from "./Loader";

const ChatPage = () => {
    const [message, setMessage] = useState('');
    const [chatHistory, setChatHistory] = useState([]);
    const [isLoading, setIsLoading] = useState(false);
    const messageInputRef = useRef(null);

    useEffect(() => {
        const chatHistoryDiv = document.querySelector('.chat-history');
        if (chatHistoryDiv) {
            chatHistoryDiv.scrollTop = chatHistoryDiv.scrollHeight;
        }
    }, [chatHistory]); // Dependency array ensures this runs every time chatHistory updates

    useEffect(() => {
        if (messageInputRef.current) {
            messageInputRef.current.focus();
        }
    }, []); // Runs once on component mount

    const handleKeyDown = (event) => {
        if (event.key === 'Enter') {
            sendMessage();
        }
    }

    const sendMessage = async () => {
        if (message.trim() === '') return;

        setIsLoading(true);

        setChatHistory(prevChatHistory => [
            ...prevChatHistory,
            { message: message, fromUser: true }
        ]);

        setMessage(''); // Clear the input field

        try {
            const response = await axios.post('http://localhost:8000/chat/query', { message });
            setChatHistory(prevChatHistory => [
                ...prevChatHistory,
                { message: response.data.message, fromUser: false }
            ]);
        } catch (error) {
            let error_message = "Error processing message: " + error.message;
            console.error(error_message);
            setChatHistory(prevChatHistory => [
                ...prevChatHistory,
                { message: error_message, fromUser: false }
            ]);
        } finally {
            setIsLoading(false);
            setTimeout(() => {
                if (messageInputRef.current) {
                    messageInputRef.current.focus();
                }
            }, 0);
        }
    };


    return (
        <div className="chat-container">
            <div className="chat-history">
                {chatHistory.map((chat, index) => (
                    <div key={index} className={`chat-message ${chat.fromUser ? 'user' : 'server'}`}>
                        {chat.message}
                    </div>
                ))}
                {isLoading && <div className="loader-container"><Loader /></div>}
            </div>
            <div className="chat-input">
                <input type="text"
                       value={message}
                       onChange={(e) => setMessage(e.target.value)}
                       disabled={isLoading}
                       onKeyDown={handleKeyDown}
                       ref={messageInputRef}
                />
                <button onClick={sendMessage} disabled={isLoading}>
                    {isLoading ? 'Awaiting Response...' : 'Send Message'}
                </button>
            </div>

        </div>
    );
};

export default ChatPage;
