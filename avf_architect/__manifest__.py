# -*- coding: utf-8 -*-
{
    'name': 'AVF Creative Architect ERP',
    'version': '18.0.1.0.0',
    'category': 'Project Management',
    'summary': 'Complete AI-Enabled Architectural ERP for Government Consultancy Projects',
    'description': """
        Advanced Architectural ERP Module for AVF Creative Firm
        =====================================================
        
        Core Features:
        * Government Project Management
        * AI-Powered Design Assistance
        * Blueprint & Drawing Management
        * Regulatory Compliance Tracking
        * Advanced Financial Management
        * Team Collaboration Tools
        * Client Portal Integration
        * Real-time Progress Tracking
        * Document Management System
        * Automated Reporting
        
        DPR & Survey Management:
        * DPR (Detailed Project Report) Creation
        * SSR/DSR Survey Report Integration
        * State/Department Specific Guidelines
        * AI-Enhanced DPR Generation
        * Survey Data Analysis & Recommendations
        * Compliance Checklist Automation
        
        FCA & Ecotourism Compliance:
        * Forest Conservation Act (FCA) Compliance
        * PARIVESH Portal Integration
        * Biodiversity Impact Assessment
        * Ecotourism Design Optimization
        * Compensatory Afforestation Planning
        * Community Engagement Strategies
        * Carbon Footprint Analysis
        * Wildlife-Friendly Design Features
        
        Rate Schedule & Estimation:
        * DSR (District Schedule of Rates)
        * SSR (State Schedule of Rates)
        * Government-Compliant Estimates
        * Rate Analysis & Validation
        * Market Rate Comparison
        * Approval Workflow Management
        * Audit-Ready Documentation
        * GST & Statutory Compliance
    """,
    'author': 'AVF Creative Solutions',
    'website': 'https://avfcreative.com',
    'depends': [
        'base',
        'project',
        'hr',
        'account',
        'sale',
        'purchase',
        'stock',
        'mail',
        'calendar',
        'hr_timesheet',
        'project_timesheet',
    ],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'data/data.xml',
        'views/menus.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'avf_architect/static/src/css/architect_style.css',
            'avf_architect/static/src/js/architect_dashboard.js',
            'avf_architect/static/src/js/ai_assistant.js',
            'avf_architect/static/src/js/drawing_viewer.js',
        ],
    },
    'demo': [
        'demo/demo_data.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
    'license': 'LGPL-3',
    'price': 2500.00,
    'currency': 'USD',
}
