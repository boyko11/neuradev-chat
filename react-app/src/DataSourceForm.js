import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import axios from 'axios';
import './DataSourceForm.css';

import Loader from './Loader';

function DataSourceForm() {
    const navigate = useNavigate();
    const [urls, setUrls] = useState([]);
    const [folderIds, setFolderIds] = useState([]);
    const [showUrlInput, setShowUrlInput] = useState(false);
    const [showFolderIdInput, setShowFolderIdInput] = useState(false);
    const [isLoading, setIsLoading] = useState(false);


    const handleAddUrl = () => {
        setShowUrlInput(true);
        setUrls([...urls, '']);
    };

    const handleAddFolderId = () => {
        setShowFolderIdInput(true);
        setFolderIds([...folderIds, '']);
    };

    const handleUrlChange = (index, event) => {
        const newUrls = [...urls];
        newUrls[index] = event.target.value;
        setUrls(newUrls);
    };

    const handleFolderIdChange = (index, event) => {
        const newFolderIds = [...folderIds];
        newFolderIds[index] = event.target.value;
        setFolderIds(newFolderIds);
    };

    const handleSubmit = async () => {
        setIsLoading(true);

        const filteredUrls = urls.filter(url => url.trim() !== '');
        const filteredFolderIds = folderIds.filter(id => id.trim() !== '');

        try {
            const response = await axios.post('http://localhost:8000/data-sources/', { urls: filteredUrls, gdrive_folder_ids: filteredFolderIds });
            console.log(response.data);
            navigate('/chat');
        } catch (error) {
            console.error('There was an error!', error);
            // Handle error
        } finally {
            setIsLoading(false);
        }
    };

    return (
        <div className="container">
            <div className="row">
                <div className="col-md-6">
                    <h3>URLs</h3>
                    {showUrlInput && urls.map((url, index) => (
                        <input
                            key={index}
                            type="text"
                            className="form-control mb-2"
                            value={url}
                            onChange={(e) => handleUrlChange(index, e)}
                        />
                    ))}
                    <button onClick={handleAddUrl} className="btn btn-link"><i className="bi bi-plus-circle"></i> Add URL</button>
                </div>
                <div className="col-md-6">
                    <h3>Google Drive Folder IDs</h3>
                    {showFolderIdInput && folderIds.map((id, index) => (
                        <input
                            key={index}
                            type="text"
                            className="form-control mb-2"
                            value={id}
                            onChange={(e) => handleFolderIdChange(index, e)}
                        />
                    ))}
                    <button onClick={handleAddFolderId} className="btn btn-link"><i className="bi bi-plus-circle"></i> Add Folder ID</button>
                </div>
            </div>
            <div className="text-center mt-4">
                {isLoading && <Loader />}
                <button onClick={handleSubmit} className="btn btn-success" disabled={isLoading}>
                    {isLoading ? 'Adding Data Sources...' : 'Save'}
                </button>
            </div>
        </div>
    );
}

export default DataSourceForm;
