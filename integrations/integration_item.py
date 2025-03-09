from datetime import datetime
from typing import Optional, List

class IntegrationItem:
    def __init__(
        self,
        id: Optional[str] = None,
        type: Optional[str] = None,
        directory: bool = False,
        parent_path_or_name: Optional[str] = None,
        parent_id: Optional[str] = None,
        name: Optional[str] = None,
        creation_time: Optional[datetime] = None,
        last_modified_time: Optional[datetime] = None,
        url: Optional[str] = None,
        children: Optional[List[str]] = None,
        mime_type: Optional[str] = None,
        delta: Optional[str] = None,
        drive_id: Optional[str] = None,
        visibility: Optional[bool] = True,
    ):
        self.id = id
        self.type = type
        self.directory = directory
        self.parent_path_or_name = parent_path_or_name
        self.parent_id = parent_id
        self.name = name
        self.creation_time = creation_time
        self.last_modified_time = last_modified_time
        self.url = url
        self.children = children
        self.mime_type = mime_type
        self.delta = delta
        self.drive_id = drive_id
        self.visibility = visibility

class ContactIntegrationItem:
    def __init__(
        self,
        id: Optional[str] = None,
        createdAt: Optional[datetime] = None,
        updatedAt: Optional[datetime] = None,
        archived: Optional[bool] = False,
        firstName: Optional[str] = None,
        lastName: Optional[str] = None,
        email: Optional[str] = None,
    ):
        self.id = id
        self.createdAt = createdAt
        self.updatedAt = updatedAt
        self.archived = archived
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
    
    def __str__(self) -> str:
        return "First name: " + self.firstName + " Last name: " + self.lastName + " Email ID: " + self.email
