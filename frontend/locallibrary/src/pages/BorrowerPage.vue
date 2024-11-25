<template>
  <div>
    <h1>Borrowed Books</h1>

    <div v-if="borrowedBooks.length === 0">
      <p>You have not borrowed any books.</p>
    </div>

    <ul v-else>
      <li v-for="book in borrowedBooks" :key="book.id" :class="{ 'overdue': book.is_overdue }">
        <p>
          <a :href="`/book-detail/${book.book}`">{{ book.title }}</a>
          <br>
          Дата возврата: {{ formatDate(book.due_back) }}
        </p>
      </li>
    </ul>
  </div>
</template>

<script>
import { ref, onMounted} from 'vue';
import { useRouter } from 'vue-router';
import axios from 'axios';
import moment from "moment";
export default {
  name: 'BorrowerPage',
  setup() {
    const borrowedBooks = ref([]);
    const errorMessage = ref(null);
    const router = useRouter();
    const isAuthenticated = () => {
      return localStorage.getItem('access_token') !== null;
    };

    const loadBorrowedBooks = async () => {
      if (!isAuthenticated()) {
        router.push('/login');
        return;
      }

      try {
        const response = await axios.get('http://127.0.0.1:8000/api/accounts/borrower/', {
          headers: {
            Authorization: `Bearer ${localStorage.getItem('access_token')}`,
          },
        });
        borrowedBooks.value = response.data;
      } catch (error) {
        if (error.response) {
          errorMessage.value = error.response.data.detail || 'Error fetching borrowed books';
        } else {
          errorMessage.value = 'Network error. Please try again.';
        }
      }

    };

    onMounted(() => {
      loadBorrowedBooks();
    });

    return {
      borrowedBooks,
      errorMessage,
    };
  },
    methods: {
      formatDate(value) {
          if (!value) return '';
          return moment(value).format('DD/MM/YYYY'); // Формат "день месяц год"
      }
    }
};
</script>

<style scoped>
ul {
  list-style-type: none;
  padding-left: 0;
}

li {
  margin-bottom: 20px;
}

p {
  margin: 5px 0;
}

.overdue {
    color: red;
}
</style>
