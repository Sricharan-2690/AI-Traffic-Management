// DOM elements
const uploadForm = document.getElementById('uploadForm');
const fileInput = document.getElementById('fileInput');
const placeholder = document.getElementById('placeholder');
const loader = document.getElementById('loader');
const results = document.getElementById('results');
const error = document.getElementById('error');
const errorMessage = document.getElementById('error-message');

// API endpoint - Use 127.0.0.1 to avoid local DNS delays
const API_URL = 'http://127.0.0.1:5000/upload';

// Helper to safely parse JSON response
async function parseResponse(response) {
    const text = await response.text();
    console.log('Raw response from server:', text);
    try {
        return JSON.parse(text);
    } catch (e) {
        console.error('Failed to parse JSON:', text);
        throw new Error('Invalid JSON from server: ' + text.substring(0, 100));
    }
}

// Event listeners
if (uploadForm) {
    uploadForm.addEventListener('submit', handleSubmit);
    console.log('✅ Form listener attached');
} else {
    console.error('❌ Could not find uploadForm element!');
}

// Handle form submission
async function handleSubmit(e) {
    // 1. IMMEDIATELY prevent reload
    if (e) e.preventDefault();
    console.log('🚀 Form submission started...');

    const selectedFiles = Array.from(fileInput.files);
    console.log(`📂 Files selected: ${selectedFiles.length}`);

    // Validate file count
    if (selectedFiles.length !== 4) {
        console.warn('⚠️ Validation failed: Not exactly 4 videos');
        alert('Please upload exactly 4 videos.');
        return false; // Extra safety to prevent submission
    }

    // Show loading state
    showLoading();

    try {
        const formData = new FormData();
        selectedFiles.forEach((file, index) => {
            console.log(`  - Adding file ${index}: ${file.name}`);
            formData.append('videos', file);
        });

        console.log('📡 Sending request to backend...');
        const response = await fetch(API_URL, {
            method: 'POST',
            body: formData
        });

        console.log(`📡 Response received. Status: ${response.status}`);

        if (!response.ok) {
            const errorText = await response.text();
            throw new Error(`Server error (${response.status}): ${errorText}`);
        }

        const result = await parseResponse(response);
        console.log('✅ Final Result Object:', result);

        if (result.error) {
            showError(result.error);
        } else {
            showResults(result);
        }

    } catch (err) {
        console.error('❌ Catch Block Error:', err);
        showError(err.message || 'Failed to upload files. Please check if the backend is running.');
    }

    return false; // Prevent default
}

// Show loading state
function showLoading() {
    console.log('⏳ Showing Loader...');
    placeholder.classList.add('hidden');
    loader.classList.remove('hidden');
    results.classList.add('hidden');
    error.classList.add('hidden');
}

// Show results
function showResults(result) {
    console.log('✨ Displaying Results in UI...');

    placeholder.classList.add('hidden');
    loader.classList.add('hidden');
    results.classList.remove('hidden');
    error.classList.add('hidden');

    // Update result values
    if (result) {
        document.getElementById('north-time').textContent = result.north ?? '--';
        document.getElementById('south-time').textContent = result.south ?? '--';
        document.getElementById('west-time').textContent = result.west ?? '--';
        document.getElementById('east-time').textContent = result.east ?? '--';
        console.log('✅ UI Updated successfully');
    }
}

// Show error
function showError(message) {
    console.error('🚑 Showing Error UI:', message);
    placeholder.classList.add('hidden');
    loader.classList.add('hidden');
    results.classList.add('hidden');
    error.classList.remove('hidden');

    errorMessage.textContent = message;
}

// Reset form and show placeholder
function resetForm() {
    uploadForm.reset();
    placeholder.classList.remove('hidden');
    loader.classList.add('hidden');
    results.classList.add('hidden');
    error.classList.add('hidden');
}

// Add file input change listener to show selected files count
fileInput.addEventListener('change', function () {
    const selectedFiles = Array.from(this.files);
    console.log(`📁 Input Changed: ${selectedFiles.length} files selected`);
});