```mermaid
flowchart TD
    A[User Enters KareerKonnect] --> B{User Type?}
    B -->|Job Seeker| C[Create/Update Profile]
    B -->|Employer| D[Post Job/Internship]
    
    C --> E[Explore Opportunities]
    E --> F[Search Jobs]
    E --> G[Find Internships]
    E --> H[Access JobDost AI Counselor]
    
    F --> I[JobDost AI Job Matching]
    G --> I
    I --> J[Apply for Positions]
    
    H --> K[Get Career Guidance]
    K --> L[Skill Development]
    K --> M[Resume Building]
    K --> N[Interview Prep]
    
    J --> O{Application Status}
    O -->|Accepted| P[Interview Process]
    O -->|Rejected| Q[Receive Feedback]
    
    D --> R[JobDost Analyzes Requirements]
    R --> S[Match with Candidates]
    S --> T[Review Applications]
    T --> U[Schedule Interviews]
    
    P --> V[MILAN Video Chat]
    U --> V
    V --> W[Conduct Interview]
    
    W --> X[Hiring Decision]
    X -->|Hired| Y[Successful Placement]
    X -->|Not Hired| Z[Provide Feedback]
    
    style A fill:#f9d71c,stroke:#333,stroke-width:2px
    style Y fill:#66c2a5,stroke:#333,stroke-width:2px
    style B fill:#8da0cb,stroke:#333,stroke-width:2px
    style I fill:#fc8d62,stroke:#333,stroke-width:2px
    style H fill:#e78ac3,stroke:#333,stroke-width:2px
    style V fill:#e74c3c,stroke:#333,stroke-width:2px
