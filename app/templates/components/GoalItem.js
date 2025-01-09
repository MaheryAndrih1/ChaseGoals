const GoalItem = ({ goal, onUpdate }) => {
    const [isEditing, setIsEditing] = useState(false);
    const [newName, setNewName] = useState(goal.name_goal);

    const formatDate = (dateString) => {
        const date = new Date(dateString);
        return date.toISOString().replace('T', ' ').split('.')[0];
    };
    
    const handleUpdate = async () => {
        try {
            const csrfToken = getCookie('csrftoken');
            if (!csrfToken) {
                throw new Error('CSRF token not found');
            }

            const response = await fetch(`/update_goal/${goal.id_goal}/`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': csrfToken,
                },
                body: JSON.stringify({ name_goal: newName }),
            });
            
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            
            const data = await response.json();
            if (data.status === 'success') {
                setIsEditing(false);
                // Format the date before triggering update
                if (data.goal && data.goal.date_created) {
                    data.goal.date_created = formatDate(data.goal.date_created);
                }
                onUpdate();
            } else {
                throw new Error('Update failed');
            }
        } catch (error) {
            console.error('Error updating goal:', error);
            alert('Failed to update goal. Please try again.');
        }
    };

    return (
        <div className="card m-2">
            <div className="card-body">
                <div className="row align-items-center">
                    <div className="col-11">
                        {isEditing ? (
                            <div>
                                <input
                                    type="text"
                                    value={newName}
                                    onChange={(e) => setNewName(e.target.value)}
                                    className="form-control"
                                />
                                <button onClick={handleUpdate} className="btn btn-primary mt-2">Save</button>
                                <button onClick={() => setIsEditing(false)} className="btn btn-secondary mt-2 ms-2">Cancel</button>
                            </div>
                        ) : (
                            <React.Fragment>
                                <div className="card-title">
                                    <h5><span>{goal.id_goal}</span> - {goal.name_goal}</h5>
                                </div>
                                <h6 className="card-subtitle mb-2 text-body-secondary">
                                    {formatDate(goal.date_created)}
                                </h6>
                            </React.Fragment>
                        )}
                    </div>
                    <div className="col-1 d-flex justify-content-end">
                        <a className="check-c me-2" href={`/achieved_goal/${goal.id_goal}/`}>
                            {goal.is_achieved ? 
                                <i className="bi bi-check-circle-fill" id="green"></i>
                                :
                                <i className="bi bi-check-circle"></i>
                            }
                        </a>
                        <div className="dropdown">
                            <button className="btn p-0 mt-2" type="button" data-bs-toggle="dropdown" aria-expanded="false">
                                <i className="bi bi-three-dots-vertical"></i>
                            </button>
                            <ul className="dropdown-menu dropdown-menu">
                                <li>
                                    <a className="dropdown-item" href={`/delete_goal/${goal.id_goal}/`}>Delete</a>
                                </li>
                                <li>
                                    <button className="dropdown-item" onClick={() => setIsEditing(true)}>Update</button>
                                </li>
                            </ul>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
};
