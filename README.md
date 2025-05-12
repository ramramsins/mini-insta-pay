# Mini-InstaPay

A digital money transfer platform designed to enable users to securely send and receive money instantly. The system supports account registration, login, balance management, transaction history tracking, and basic reporting.

## Architecture

The system is built using a microservices architecture with the following components:

1. **User Service** (Port: 8000)
   - Handles user registration and authentication
   - Manages user profiles and account details
   - Provides user-related operations

2. **Transaction Service** (Port: 8001)
   - Manages money transfers between users
   - Handles balance updates
   - Maintains transaction logs

3. **Reporting Service** (Port: 8002)
   - Generates transaction reports
   - Provides analytics and insights
   - Handles data aggregation

## Prerequisites

- Docker and Docker Compose
- Kubernetes (for production deployment)
- MongoDB
- Python 3.8+

## Environment Setup

The project supports three environments:

1. **Development**
   ```bash
   docker-compose -f docker-compose.dev.yml up
   ```

2. **Staging**
   ```bash
   docker-compose -f docker-compose.staging.yml up
   ```

3. **Production**
   ```bash
   docker-compose -f docker-compose.prod.yml up
   ```

## Monitoring and Logging

The system includes comprehensive monitoring and logging capabilities:

### Prometheus & Grafana
- Prometheus is available at: http://localhost:9090
- Grafana dashboard is available at: http://localhost:3000
  - Default credentials: admin/admin

### ELK Stack
- Elasticsearch is available at: http://localhost:9200
- Kibana is available at: http://localhost:5601

## API Documentation

### User Service Endpoints
- POST /api/users/register - Register a new user
- POST /api/users/login - User login
- GET /api/users/{user_id} - Get user details
- PUT /api/users/{user_id} - Update user details

### Transaction Service Endpoints
- POST /api/transactions - Create a new transaction
- GET /api/transactions/{transaction_id} - Get transaction details
- GET /api/transactions/user/{user_id} - Get user's transactions

### Reporting Service Endpoints
- GET /api/reports/transactions - Get transaction reports
- GET /api/reports/users/{user_id} - Get user-specific reports

## Development

1. Clone the repository
2. Set up the development environment:
   ```bash
   docker-compose -f docker-compose.dev.yml up
   ```

3. Access the services:
   - User Service: http://localhost:8000
   - Transaction Service: http://localhost:8001
   - Reporting Service: http://localhost:8002

## Deployment

### Kubernetes Deployment
1. Apply the Kubernetes configurations:
   ```bash
   kubectl apply -f k8s/
   ```

2. Verify the deployment:
   ```bash
   kubectl get pods
   kubectl get services
   ```

## Monitoring and Alerts

The system includes:
- Service health monitoring
- Performance metrics
- Error tracking
- Resource utilization monitoring

Access monitoring dashboards:
- Grafana: http://localhost:3000
- Prometheus: http://localhost:9090
- Kibana: http://localhost:5601

## Security

- All services use secure communication
- Environment-specific credentials
- Regular security updates
- Access control and authentication

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details. 