document.getElementById("fileInput").addEventListener("change", function(event) {
    const fileInput = event.target;
    const file = fileInput.files[0];
    
    // Check if a file is selected
    if (file) {
        const reader = new FileReader();
        
        // On file load, show the image preview
        reader.onload = function(e) {
            const imagePreviewContainer = document.getElementById("imagePreviewContainer");
            const imagePreview = document.getElementById("imagePreview");
            const convertButton = document.getElementById("convertButton");

            // Display the image preview and enable the button
            imagePreviewContainer.style.display = "block";
            imagePreview.src = e.target.result;
            
            // Show the Convert to CSV button
            convertButton.style.display = "block";
        };

        // Read the file as a data URL to show the image
        reader.readAsDataURL(file);
        
        // Optional: Check if the image clarity is acceptable
        checkImageClarity(file);
    }
});

function checkImageClarity(file) {
    const clarityMessage = document.getElementById("clarityMessage");
    
    // Here, you can add logic to assess the clarity of the image
    // For now, let's assume the image clarity is good (you can replace this with actual logic)
    if (file.size < 500000) {  // Example: Checking if the image is too small (not clear)
        clarityMessage.textContent = "Please upload a clearer image (larger file).";
    } else {
        clarityMessage.textContent = "";  // Clear any previous message
    }
}
