<script lang="ts">
	import { PUBLIC_BACKEND_URL } from '$env/static/public';

	let loginForm: HTMLFormElement;
	async function login(event: SubmitEvent) {
		event.preventDefault();
		const loginData = new FormData(loginForm);
		const res = await fetch(`${PUBLIC_BACKEND_URL}/login`, {
			method: 'POST',
			credentials: 'include',
			// headers: {
			// 	'Content-Type': 'application/x-www-form-urlencoded'
			// },
			body: loginData
		});
		if (res.status == 200) {
		}
		// console.log(formDatla);
		// console.log(new URLSearchParams(formData).toString());
	}
</script>

<div class="absolute left-1/2 top-1/3">
	<form
		bind:this={loginForm}
		onsubmit={login}
		class="relative right-1/2 flex flex-col gap-3 rounded-lg bg-blue-400 p-10"
		action="{PUBLIC_BACKEND_URL}/login"
		method="POST"
	>
		<div>
			<label for="username">Username</label>
			<input class="rounded-md bg-white p-1" type="text" id="username" name="username" required />
		</div>

		<div>
			<label for="password">Password</label>
			<input
				class="rounded-md bg-white p-1"
				type="password"
				id="password"
				name="password"
				required
			/>
		</div>

		<button class="w-fit cursor-pointer self-center rounded-md bg-emerald-200 p-2" type="submit"
			>Login</button
		>
	</form>
</div>
